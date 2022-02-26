import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open("sizeOfTV_watchingHrs.csv", newline='') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Size of TV", y = "Average time")
        fig.show()

def getDataSource(data_path):
    sizeOfTv = []
    averageTimeSpent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeOfTv.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["Average time"]))
    
    return {"x": sizeOfTv, "y": averageTimeSpent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The correlation between the size of TV and hours spent watching it is", correlation[0,1])

def setup():
    data_path = "sizeOfTV_watchingHrs.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)