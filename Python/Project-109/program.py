import pandas as pd
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
score_list = df["math score"].tolist()

score_mean = statistics.mean(score_list)
score_median = statistics.median(score_list)
score_mode = statistics.mode(score_list)
score_stddev = statistics.stdev(score_list)

print(score_mean)
print(score_median)
print(score_mode)
print(score_stddev)

#first standard deviation
score_first_stddev_start, score_first_stddev_end = score_mean - score_stddev, score_mean + score_stddev
#second standard deviation
score_second_stddev_start, score_second_stddev_end = score_mean - (2*score_stddev), score_mean + (2*score_stddev)
#third standard deviation
score_third_stddev_start, score_third_stddev_end = score_mean - (3*score_stddev), score_mean + (3*score_stddev)

score_listOfData_within_first_stddev = [result for result in score_list if result > score_first_stddev_start and result < score_first_stddev_end]
scorelistOfData_within_second_stddev = [result for result in score_list if result > score_second_stddev_start and result < score_second_stddev_end]
score_listOfData_within_third_stddev = [result for result in score_list if result > score_third_stddev_start and result < score_third_stddev_end]

print("{}% of data for math scores lies within 1 standard deviation".format(len(score_listOfData_within_first_stddev)*100.0/len(score_list))) 
print("{}% of data for math scores lies within 2 standard deviations".format(len(scorelistOfData_within_second_stddev)*100.0/len(score_list))) 
print("{}% of data for math score lies within 3 standard deviations".format(len(score_listOfData_within_third_stddev)*100.0/len(score_list)))

#fig = ff.create_distplot([score_list], ["result"])
#fig.show()