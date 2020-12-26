# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:19:30 2019

@author: matth
"""
"""The objective of this program is to calculate the population of the bears,
berries and the tourist in a certain location according to a correlation that
occurs between all three"""

"""import statement takes the log and trunc function from the syllables class"""
from math import log,trunc

#sets the following variables equal to 0 in order to be used later in my program
tourists = 0
bears_next = 0
berries_next = 0

"""The objective of this function is to return the number of tourist according to the number of bears"""
def tourist_pop(bears):
    if bears < 4 or bears > 15:
        tourists = 0 
        return tourists
    elif bears <= 10 and bears >= 4:
        tourists = 10000 * bears
        return tourists
    elif bears > 10:
        tourists = 100000 + (20000 * (bears-10))
        return tourists

"""The objective of this function is to return a tuple representing the number of
bears and berries in the following year according to the correlation between both(formula)"""
def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (log(1+tourists,10)*0.1)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - (log(1+tourists,10)*0.05)
    #print(berries_next)

    next_year = (bears_next,berries_next)
    return next_year

#user inputs to represent original number of bears and berries in location  
OG_bears = int((input("Number of bears => ")))
print(OG_bears)
OG_berries = input("Size of berry area => ")
print(OG_berries)
OG_berries = float(OG_berries)

#lists created corresponding to each species containing the original number
bears_list = [OG_bears]
berries_list = [OG_berries]
tourists_list = [tourist_pop(OG_bears)]

#print original popultion of each species
print("Year\tBears\tBerry\tTourists")
print("1\t{0:d}\t{1:.1f}\t{2:d}".format(OG_bears,OG_berries,tourist_pop(OG_bears)))

#variable for next bears and next berries according to function
bears,berries = find_next(OG_bears,OG_berries,tourist_pop(OG_bears))
#for loops runs through years 2-10(inclusive) printing out the population of each specis
for i in range(2,11):
    bears = trunc(bears)
    bears_list.append(bears)
    tourists_list.append(tourist_pop(bears))
    if berries < 0:
        berries = 0
    print(str(i) + "\t{0:.0f}\t{1:.1f}\t{2:.0f}".format(bears,berries,tourist_pop(bears)))
    berries_list.append(berries)
    bears,berries = find_next(bears,berries,tourist_pop(bears))
print("")
#print max and min population in each list of species
print("Min:\t{0:}\t{1:.1f}\t{2:}".format(min(bears_list),min(berries_list),min(tourists_list)))       
print("Max:\t{0:}\t{1:.1f}\t{2:}".format(max(bears_list),max(berries_list),max(tourists_list))) 