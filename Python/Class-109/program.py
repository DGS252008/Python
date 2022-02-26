import pandas as pd
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].tolist()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)
height_stddev = statistics.stdev(height_list)

print(height_mean)
print(height_median)
print(height_mode)
print(height_stddev)

#fig = ff.create_distplot([height_list], ["result"])
#fig.show()
#first standard deviation
height_first_stddev_start, height_first_stddev_end = height_mean - height_stddev, height_mean + height_stddev
#second standard deviation
height_second_stddev_start, height_second_stddev_end = height_mean - (2*height_stddev), height_mean + (2*height_stddev)
#third standard deviation
height_third_stddev_start, height_third_stddev_end = height_mean - (3*height_stddev), height_mean + (3*height_stddev)

height_listOfData_within_first_stddev = [result for result in height_list if result > height_first_stddev_start and result < height_first_stddev_end]
height_listOfData_within_second_stddev = [result for result in height_list if result > height_second_stddev_start and result < height_second_stddev_end]
height_listOfData_within_third_stddev = [result for result in height_list if result > height_third_stddev_start and result < height_third_stddev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_listOfData_within_first_stddev)*100.0/len(height_list))) 
print("{}% of data for height lies within 2 standard deviations".format(len(height_listOfData_within_second_stddev)*100.0/len(height_list))) 
print("{}% of data for height lies within 3 standard deviations".format(len(height_listOfData_within_third_stddev)*100.0/len(height_list)))

