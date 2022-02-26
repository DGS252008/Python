import csv

with open("hwdata.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

total = 0
n = len(new_data)
for i in range(len(new_data)):
    total += i

mean = total/n

print(mean)