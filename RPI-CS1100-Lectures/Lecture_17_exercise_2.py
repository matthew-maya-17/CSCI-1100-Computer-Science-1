# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:18:46 2019

@author: matth
"""

file = input('Enter the name of the IMDB file ==> ').strip()
print (file)
total_Movies = dict()
for line in open(file, encoding = "ISO-8859-1"):
    tempList = line.strip().split('|')
    movie = tempList[1].strip()
    name = tempList[0].strip()
    if movie not in total_Movies:
        total_Movies[movie] = set({name})
    else:
        total_Movies[movie].add(name)

number = 0
maxName = ''
for place in total_Movies:
    total = len(total_Movies[place])
    if total > number:
        number = total
        maxName = place
print (number)
print (maxName)
count = 0
for val in total_Movies:
    if (len(total_Movies[val])) == 1:
        count += 1
print (count)