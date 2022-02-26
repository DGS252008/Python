import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random 
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print("The mean is " , mean)
print("The standard deviation is " , stdev)

def random_mean(): 
    sample_data = [] 
    for i in range(0,100): 
        random_index = random.randint(0,len(data)-1) 
        value = data[random_index] 
        sample_data.append(value) 
        sample_mean = statistics.mean(sample_data) 
        #sample_stdDEv = statistics.stdev(sample_data)
        return sample_mean 

mean_list=[] 
for i in range(0,1000): 
    all_mean_data = random_mean() 
    mean_list.append(all_mean_data) 
    final_mean = statistics.mean(mean_list) 
    final_stdDev = statistics.stdev(mean_list) 
    print("sampling mean:- ",final_mean,"sampling stdDev: ",final_stdDev) 
    
fig = ff.create_distplot([mean_list], ["Math scores"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.20], mode = "lines", name = "Mean"))
fig.show()
