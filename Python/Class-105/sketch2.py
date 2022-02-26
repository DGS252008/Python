import csv

with open("class2.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
totalMarks = 0

for marks in file_data:
    totalMarks += float(marks[1])

total = 0
n = len(file_data)

mean = totalMarks/n

print("The mean is " + str(mean))

import pandas as pd 
import plotly.express as px 

df = pd.read_csv('class2.csv')

fig = px.scatter(df, x="Student Number", y="Marks", title="Marks in Class 2")
fig.update_layout(shapes = [
    dict(
        type = "line",
         y0 = mean, y1 = mean, 
         x0 = 0, x1 = n
    )
])
fig.update_yaxes(rangemode = "tozero")
fig.show()