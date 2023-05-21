# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:28:25 2019

@author: matth
"""
file_name = str(input("Data file name: ")).strip()
print(file_name)
prefix = str(input("Prefix: ")).strip()
print(prefix)

names = set()
last_names = set()
counter = 0
for line in open(file_name, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].split(",")
    last_name = name[0]
    last_names.add(last_name)
    if prefix in last_names:
        counter += 1
print(len(last_names), "last names")
print("{} start with {}".format(counter, prefix)) #IDK how to search for just part of a value in a set