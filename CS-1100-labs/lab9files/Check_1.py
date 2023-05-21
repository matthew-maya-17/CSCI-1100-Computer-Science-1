# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 01:34:17 2019

@author: matth
"""
import math
def closest1(LIST):
    '''
    closest1(LIST) returns a tuple containing the two closest values 
    that are passed in the list LIST

    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    >>> closest1([1.3,24,53,2.4])
    (1.3, 2.4)
    >>> closest1([-1.37,-234,-5,-27.5,-7834,-8.93,-467,-24.6,-100])
    (-27.5, -24.6)
    >>> closest1([])
    (None, None)
    >>> closest1([1.2,1.4,1.3,5])
    (1.4, 1.3)
    >>> closest1([7.2,7.5,7.6,5])
    (7.5, 7.6)
    '''
    specific_x = None
    specific_y = None
    if len(LIST) < 2:
        return (specific_x, specific_y)
    minimum = float(math.inf)
    for x in range(len(LIST)):
        for y in range(len(LIST)):
            if x != y:
                subtracted = abs(LIST[x] - LIST[y])
                if subtracted < minimum:
                    minimum = subtracted
                    specific_x = LIST[x]
                    specific_y = LIST[y]
    return (specific_x, specific_y)
           
if __name__ == "__main__":
    print(closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]))
    print(closest1([1.3,24,53,2.4]))
    print(closest1([-1.37,-234,-5,-27.5,-7834,-8.93,-467,-24.6,-100]))
    print(closest1([]))
    print(closest1([1.2,1.4,1.3,5]))
    print(closest1([7.2,7.5,7.6,5]))