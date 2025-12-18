# Final Project

## Groupe 2 Ing5 Data-IA
## Authors
- Rémy Chen
- Pavan Wickramasinghage
- Hadrien Lagadec
- Lucas Lorang

[Github Project](https://github.com/Luckuah/Big_Data_framework.git)

## For the scoring part

### 📦 Installation

1. Clone the repository:
   
```bash
git clone https://github.com/Luckuah/Big_Data_framework.git
```
2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate      # On Windows
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### To run the code 

(In your repository)

```bash
jupyter notebook
```

## For the streaming part

  If you have a containeur with a same name it will delete it

  ```bash
  docker rm -f wiki-container
  ```

  Build the containeur

  ```bash
  docker build -t wiki-spark-stream .
  ```

  Run the containeur

  ```bash
  docker run -it --name wiki-container -v "$($PWD)\stream_wiki_output:/app/wiki_spark_output" wiki-spark-stream
  ```
