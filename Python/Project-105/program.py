import csv 
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#new code
data=[]
total_marks = 0
for i in range(len(file_data)):
    num = file_data[i][0]
    data.append(int(num))
    total_marks += float(file_data[i][0])

total_entries = len(data)

mean = total_marks/total_entries

squared_list = []
for number in data:
    a = int(number) - mean
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum+i

result = sum/(len(data)-1)

std_dev = math.sqrt(result)
print(std_dev)
