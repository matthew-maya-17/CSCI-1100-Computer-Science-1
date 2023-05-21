# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:22:19 2019

@author: matth
"""

def first_day_greater(l1,l2):
    i = 0
    while i < len(l1) and i < len(l2):
        if l1[i] > l2[i]:
            return i
        i = i + 1
    return -1
            
if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))