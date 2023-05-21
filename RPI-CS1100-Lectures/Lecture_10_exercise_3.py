# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:07:00 2019

@author: matth
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

average = sum(co2_levels)/len(co2_levels)
counter = 0
for i in co2_levels:
    if i > average:
        counter += 1
print("Average: {:.2f}".format(average))
print("Num above average: "+ str(counter))