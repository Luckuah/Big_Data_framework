import json
import os
from datetime import datetime
from requests_sse import EventSource
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count,lit


spark = SparkSession.builder \
    .appName("WikiSparkStream") \
    .master("local[*]") \
    .getOrCreate()

url = "https://stream.wikimedia.org/v2/stream/recentchange"

track_entities = [
    "Netflix",
    "Star Wars",
    "The Godfather",
    "Comedy",
    "Christopher Nolan"
]


alert_user = "abc_user"

stream_wiki_output = "wiki_spark_output"
METRICS_PATH = f"{stream_wiki_output}/metrics"
ALERTS_PATH = f"{stream_wiki_output}/alerts"

os.makedirs(stream_wiki_output, exist_ok=True)

batch_size = 10   # micro-batch size




def is_tracked_entity(title: str) -> bool:
    return any(e.lower() in title.lower() for e in track_entities)


def process_batch(events: list):
    """Process a micro-batch of events using Spark."""
    if not events:
        return

    df = spark.createDataFrame(events)

    batch_time = datetime.now().isoformat()

    # Metrics
    metrics_df = df.groupBy("entity").agg(
        count("*").alias("edit_count")
    ).withColumn("batch_timestamp", lit(batch_time)) 

    metrics_df.write.mode("append").json(METRICS_PATH)

    # Alerts
    alerts_df = df.filter(
        (col("user") == alert_user) | (col("bot") == True)
    )

    alerts_df.write.mode("append").json(ALERTS_PATH)

    print(f"Processed batch of {len(events)} events")



headers = {
    "Accept": "text/event-stream",
    "User-Agent": "WikiSparkStream/1.0 (student project)"
}


def stream_events():
    """Read Wikimedia SSE stream and create micro-batches."""
    buffer = []

    print("Starting Wikimedia SSE stream with Spark processing...")
    print("Tracking:", track_entities)

    with EventSource(url, headers=headers) as stream:
        for event in stream:
            try:
                change = json.loads(event.data)
            except ValueError:
                continue
            
            if change["meta"]["domain"] == "canary":
                continue

            title = change.get("title", "")
            
            if not is_tracked_entity(title):
                continue

            record = {
                "timestamp": datetime.now().isoformat(),
                "entity": title,
                "user": change.get("user"),
                "bot": change.get("bot", False),
                "comment": change.get("comment", "")
            }

            buffer.append(record)

            if len(buffer) >= batch_size:
                process_batch(buffer)
                buffer.clear()


if __name__ == "__main__":
    stream_events()