# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:52:02 2019

@author: matth
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
times_actor_appears = 0
actor = ''
one_appearance = 0    
        
for name in counts:
    if counts[name] > times_actor_appears:
        times_actor_appears = counts[name]
        actor = name
print("{} appears most often: {} times".format(actor, times_actor_appears)) 

for index in range(len(names)):
    name = names[index]
    if counts[name] == 1:
        one_appearance += 1
print("{} people appear once".format(one_appearance))