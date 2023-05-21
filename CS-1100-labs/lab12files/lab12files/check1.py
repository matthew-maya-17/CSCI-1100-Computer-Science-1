# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:32:24 2019

@author: jglas
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1)+1
    
def mult(m,n):
    if n == 0:
        return 0
    else:
        return mult(m,n-1) + m

def power(x,n):
    if n == 0:
        return 1
    else:
        return power(x,n-1) * x

if __name__ == "__main__":
    print(add(5,3))
    print(mult(5,3))
    print(power(6,3))