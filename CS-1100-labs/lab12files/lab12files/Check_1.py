# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:12:36 2019

@author: matth
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1


def multiply(x,y): 
    if(y == 0): 
        return 0
    if(y > 0 ): 
        return (x + multiply(x, y - 1)) 
    if(y < 0 ): 
        return -multiply(x, -y) 
      
def power(x,n):
    if n == 0:
        return 1
    else:
        return power(x,n-1) * x
print(add(5,3))
print(multiply(8, 3)) 
print(power(6,3))