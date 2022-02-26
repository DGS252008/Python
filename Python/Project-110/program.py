import pandas as pd
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The population mean of this data is " + str(population_mean))

def showFig(data): 
    fig =ff.create_distplot([data], ["reading_time"], show_hist=False)
    fig.show()

def random_mean():
    sample_data = []
    for i in range(0, 30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        sample_data.append(value)
    sample_data_mean = statistics.mean(sample_data)

    return sample_data_mean

def large_sample_mean():
    data_set = []
    for i in range(0, 100):
        all_mean = random_mean()
        data_set.append(all_mean)
    final_mean = statistics.mean(data_set)
    final_stdev = statistics.stdev(data_set)

    print("The sample mean of this data is " + str(final_mean))

    showFig(data_set)

large_sample_mean()




