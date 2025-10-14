# Lab-1-Unstructured-data-analysis-with-RDDs-with-Docker-

## Groupe 2 Ing5 Data-IA
## Authors
- Rémy Chen
- Pavan Wickramasinghage
- Hadrien Lagadec
- Lucas Lorang

[Github Project](https://github.com/Luckuah/Lab-1-Unstructured-data-analysis-with-RDDs-with-Docker-)

### To run the notebook

From your project folder, launch the following command:

```powershell
docker run -it -p 8888:8888 -v ${PWD}:/home/jovyan/work quay.io/jupyter/pyspark-notebook:latest
```

Note: If ${PWD} does not work in PowerShell, replace it with the absolute path to your project folder. For example:

```powershell
docker run -it -p 8888:8888 -v C:\Users\YourName\Path\To\Project:/home/jovyan/work quay.io/jupyter/pyspark-notebook:latest
```
