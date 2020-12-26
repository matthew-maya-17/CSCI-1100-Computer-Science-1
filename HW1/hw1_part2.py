# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:15:31 2019

@author: matthew maya
"""
import math

minutes = input('Minutes ==> ')
print(minutes)
minutes = int(minutes)
seconds = input('Seconds ==> ') 
print(seconds)
seconds = int(seconds)
miles = input('Miles ==> ')
print(miles)
miles = float(miles)
target_miles = input('Target Miles ==> ')
print(target_miles)
target_miles = float(target_miles)

print("")

pace = math.modf((minutes + (seconds/60)) / miles)
print("Pace is", int(pace[1]),"minutes and",int(pace[0] * 60),"seconds per mile.")

speed = (miles / (minutes + (seconds/60))) * 60
print("Speed is {0:.2f} miles per hour.".format(speed))

target_distance_time = math.modf(((minutes + (seconds/60)) / miles) * target_miles)
target_distance_minutes = int(target_distance_time[1])
target_distance_seconds = int(target_distance_time[0] * 60)
#print("Time to run the target distance of", target_miles,"miles is",int(target_distance_time[1]),"minutes and", int(target_distance_time[0] * 60), "seconds.")
print("Time to run the target distance of {0:.2f} miles is {1:d} minutes and {2:d} seconds.".format(target_miles,target_distance_minutes,target_distance_seconds))