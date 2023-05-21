# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:29:52 2019

@author: matth
"""

LIST = []
x = input("Enter a value (0 to end): ")
print(x)
x = float(x)
while x != 0:
    LIST.append(x)
    x = input("Enter a value (0 to end): ")
    print(x)
    x = float(x)
print("Min: {:.0f}".format(min(LIST)))
print("Max: {:.0f}".format(max(LIST)))
print("Avg: {:.1f}".format((sum(LIST)/(len(LIST)))))