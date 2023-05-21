# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:32:07 2019

@author: matth
"""

num1 = input('Enter the first number: ')
print(num1)
num2 = input('Enter the second number: ')
print(num2)

if float(num1) > 10 and float(num2) > 10:
    print("Both are above 10.")
elif float(num1) <= 10 and float(num2) <= 10:
    print("Both are below 10.")
average = "{:.2f}".format(((float(num1)+float(num2))/2))
print("Average is", average)