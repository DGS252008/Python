import csv
from collections import Counter

with open("hwdata.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

data = Counter(new_data)
mode_data_range = {
    "110-120": 0,
    "120-130": 0,
    "130-140": 0
}

for height, occurance in data.items():
    if 50 < float(height) < 60:
         mode_data_range["110-120"] += occurance
    elif 60 < float(height) < 70:
         mode_data_range["120-130"] += occurance 
    elif 70 < float(height) < 80: 
         mode_data_range["130-140"] += occurance

print(mode_data_range.items())

mode_range, mode_occurance = 0,0 
for range,occurence in mode_data_range.items(): 
    if occurence > mode_occurance: 
        mode_range,mode_occurance = [int(range.split("-")[0]),int(range.split("-")[1])], occurence 

mode = float((mode_range[0] + mode_range[1]) / 2) 
        
print(mode)