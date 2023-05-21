# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:58:02 2019

@author: matth
"""

first_name = input("Enter your first name: ")
print(first_name)
last_name = input("Enter your first name: ")
print(last_name)

x = max(len(first_name),len(last_name),len("Hello,"))

print("*" * 3 + "*" * x + "*" * 3)
print("*" * 2, "Hello," + " "+ " " * (x-len("Hello,")) + "*" * 2)
print("*" * 2, first_name + " " + " " * (x-len(first_name)) + "*" * 2)
print("*" * 2, last_name + " " + " " * (x-len(last_name)) + "*" * 2)
print("*" * 3 + "*" * x + "*" * 3)