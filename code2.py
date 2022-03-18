from unittest import result
import pandas as pa
import csv
import statistics 

df = pa.read_csv("data 2.csv")
weightlist = df["Weight"].tolist();

#mean , median, mode for weight
wMean = statistics.mean(weightlist)
wMode = statistics.mode(weightlist)
wMedian = statistics.median(weightlist)
print("Mean,Median and Mode of Weight is{}, {} and {}respectively".format(wMean,wMedian,wMode));

#Actual stdev for weight colum
wstd = statistics.stdev(weightlist)

w_first_std_start = wMean - wstd
w_first_std_end = wMean + wstd

w_second_std_start = wMean - (2*wstd)
w_second_std_end = wMean + (2*wstd)

w_third_std_start = wMean - (2*wstd)
w_third_std_end = wMean + (2*wstd)

#percentage of data within 1, 2  and 3 standard Deviations for Weight
weight_list_of_data_first = [result for result in weightlist if result > w_first_std_start and result< w_first_std_end]
weight_list_of_data_second = [result for result in weightlist if result > w_second_std_start and result< w_second_std_end]
weight_list_of_data_third = [result for result in weightlist if result > w_third_std_start and result< w_third_std_end]

print("{}% of data for weight lies within 1st standard deviation".format(len(weight_list_of_data_first)*100.0/len(weightlist)))
print("{}% of data for weight lies within 2nd standard deviation".format(len(weight_list_of_data_second)*100.0/len(weightlist)))
print("{}% of data for weight lies within 3rd standard deviation".format(len(weight_list_of_data_third)*100.0/len(weightlist)))