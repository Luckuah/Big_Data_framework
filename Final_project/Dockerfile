FROM python:3.10-slim

RUN apt-get update && apt-get install -y default-jre && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY stream_wiki.py /app/


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "stream_wiki.py"]
