# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:33:55 2019

@author: matth
"""
"""The objective of this program is ask the user for his university and then two numerical 
digits that will represent two universities from 1-1000. After the universities have been
selected all three will be compared using the data list"""

import hw4_util

data = hw4_util.read_university_file("university_data.csv")

"""The objective of this function is to return the index of the list if the university
name is contained in the list data otherwise it will return -1"""
def find_university(data, uname):
    for index_value in data:
        if index_value[0] == uname:
            return data.index(index_value)
    return -1

#all the user input followed by a print stateent
university = input("University name => ")
print(university)
first_university = int(input("Line number for first university to compare (1-1000) => "))
print(first_university)
second_university = int(input("Line number for second university to compare (1-1000) => "))
print(second_university)

#if the university name is not found in the data list then print University not found
#otherwise print both university names along with the comparison of all three universities
if find_university(data, university) == -1:
    print("University not found")
else:
    print("First university: " + data[first_university][0])
    print("Second university: " + data[second_university][0])
    print("")
    print("{0:>25}{1:>12}{2:>12}{3:>12}".format("","First","Second", "Yours"))
    for i in range(1,14):
        print("{0:>25}{1:>12}{2:>12}{3:>12}".format(data[0][i],data[first_university][i],data[second_university][i],data[find_university(data, university)][i]))