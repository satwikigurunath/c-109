from unittest import result
import pandas as pa
import csv
import statistics 

df = pa.read_csv("data 2.csv")
heightList = df["Height"].tolist();

#mean, median, mode
hMean = statistics.mean(heightList)
hMode = statistics.mode(heightList)
hMedian = statistics.median(heightList)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(hMean,hMedian, hMode));

#Actual Stdev for the height column
hStd = statistics.stdev(heightList);

h_first_std_start = hMean - hStd
h_first_std_end = hMean + hStd

h_second_std_start = hMean-(2*hStd)
h_second_std_end = hMean +(2*hStd)

h_third_std_start = hMean-(3*hStd)
h_third_std_end = hMean +(3*hStd)

#Percentage of data within 1, 2 and 3 Standard Deviations for Height
height_list_of_data_first = [result for result in heightList if result > h_first_std_start and result < h_first_std_end]
height_list_of_data_second = [result for result in heightList if result > h_second_std_start and result < h_second_std_end]
height_list_of_data_third = [result for result in heightList if result > h_third_std_start and result < h_third_std_end]

print("{}% of data for height lies within 1st standard deviation".format(len(height_list_of_data_first) * 100.0 / len(heightList)))
print("{}% of data for height lies within 2nd standard deviation".format(len(height_list_of_data_second) * 100.0 / len(heightList)))
print("{}% of data for height lies within 3rd standard deviation".format(len(height_list_of_data_third) * 100.0 / len(heightList)))