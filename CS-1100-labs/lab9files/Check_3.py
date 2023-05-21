# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:42:47 2019

@author: matth
"""

import random
def closest1(L1):
    """
    closest1(L1) is a function that takes in a list of integers or floats 
    and returns the two closest values from the list
    
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    >>> closest1([ 1.2, 1.7, 1.8, 45 ])
    (1.8, 1.7)
    >>> closest1([ 2.1, 2, 1, 3, 4 ])
    (2.1, 2)
    >>> closest1([ 70, 30, 1000, 1400, 45000 ])
    (70, 30)
    >>> closest1([ 55.3, 47, 32.8, 21, 15, 14, 7])
    (15, 14)
    >>> closest1([ 75, 76, 1, 5])
    (76, 75)
    """
    current_diff = 100000000000000
    if len(L1) < 2:
        return ("None", "None")
    else:
        for i in range(0,len(L1)):
            for j in range(0,len(L1)):
                diff1 = L1[j]-L1[i]
                if diff1 < current_diff and diff1 > 0:
                    current_diff = diff1
                    y = L1[i]
                    x = L1[j]        
    return(x,y)
           
def closest2(L1):
    """
    closest2(L2) is a function that takes in a list of integers or floats,
    sorts the list, and returns the two closest values from the list
    
    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    >>> closest2([ 1, 23, 4, 3, 10 ])
    (4, 3)
    >>> closest2([ 55.0, 3, 23, 1, 3.2 ])
    (3.2, 3)
    >>> closest2([])
    ('None', 'None')
    >>> closest2([ 45, 1, 70, 4, 55 ])
    (4, 1)
    >>> closest2([ 100, 70, 50, 10, 9, 4])
    (10, 9)
    """
    current_diff = 100000000000000
    if len(L1) < 2:
        return ("None","None")
    else:
        L2 = sorted(L1)
        for i in range(0,len(L2)):
            for j in range(0,len(L2)):
                diff1 = L2[j]-L2[i]
                if diff1 < current_diff and diff1 > 0:
                    current_diff = diff1
                    y = L2[i]
                    x = L2[j]
    return (x,y)             

if __name__ in "__main__":
    pass
    L1 = []
    L2 = []
    L3 = []
    
    for i in range(0,99):
        L1.append(random.uniform(0.0, 1000.0))
    for i in range(0,999):
        L2.append(random.uniform(0.0, 1000.0))
    for i in range(0,9999):
        L3.append(random.uniform(0.0, 1000.0))    

    (x, y) = closest1(L1)
    print(x, y)
    
    (x2, y2) = closest2(L1)
    print(x2, y2)
    
    
    (x, y) = closest1(L2)
    print(x, y)
    
    (x2, y2) = closest2(L2)
    print(x2, y2)    
    
    
    (x, y) = closest1(L3)
    print(x, y)
    
    (x2, y2) = closest2(L3)
    print(x2, y2)
    
