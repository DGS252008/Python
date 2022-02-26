import csv
import math

with open("class105Data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
data = file_data[0]
totalMarks = 0

print(data)

for marks in file_data:
    totalMarks += float(marks[1])
s
total = 0
n = len(file_data)

mean = totalMarks/n
#print(mean)

# subtract mean from each item
squaredlist = []
for number in file_data:
    #print(number)
    a = float(number) - float(mean)
    print(a)
    a = a**2 
    squaredlist.append(a)
#print(squaredlist)

#sum of all the squared data
sum = 0
for i in squaredlist:
    sum = sum+i
#print(sum)

#dividing sum by n-1
result = sum/n-1

#sqrt
Std_dev = math.sqrt(result)

print(Std_dev)
