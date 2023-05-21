# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:00:57 2019

@author: matth
"""

import math
def closest2(LIST):
    '''
    closest2(LIST) makes a copy of LIST and then sorts it in order to 
    return a tuple containing the two closest values that are passed in the list LIST

    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    >>> closest2([1.3,24,53,2.4])
    (1.3, 2.4)
    >>> closest2([])
    (None, None)
    >>> closest2([1.2,1.4,1.3,5])
    (1.3, 1.4)
    >>> closest2([7.2,7.5,7.6,5])
    (7.5, 7.6)
    '''
    list2 = LIST.copy()
    list2.sort()
    specific_x = None
    if len(list2) < 2:
        return (specific_x, specific_x)
    minimum = float(math.inf)
    for x in range(len(list2)):
        if x == len(list2) - 1:
            break
        subtracted = abs(list2[x] - list2[x+1])
        if subtracted < minimum:
            minimum = subtracted
            specific_x = list2[x]
            specific_y = list2[x+1]
    return (specific_x, specific_y)

if __name__ == "__main__":
    print(closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]))
    print(closest2([1.3,24,53,2.4]))
    print(closest2([-1.37,234,5,27.5,7834,8.93,467,24.6,100]))
    print(closest2([]))
    print(closest2([1.2,1.4,1.3,5]))
    print(closest2([7.2,7.5,7.6,5]))