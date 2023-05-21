# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:01:43 2019

@author: matth
"""
#list
values = [ 14, 10, 8, 19, 7, 13 ]

#Step 1
first_value = int(input("Enter a value: "))
print(first_value)
values.append(first_value)

#Step 2
second_value = int(input("Enter another value: "))
print(second_value)
values.insert(2, second_value)


#Step 3
print(values[3], values[-1])

#Step 4
print("Difference: " + str(max(values) - min(values)))

#Step 5
average = round(sum(values)/len(values),1)
print("Average: " + str(average))

#Step 6

values.sort()
median_low = values[int((len(values) - 1)/2)]
median_high = values[int((len(values))/2)]
median = (median_low + median_high)/2
print("Median: " + str(median))