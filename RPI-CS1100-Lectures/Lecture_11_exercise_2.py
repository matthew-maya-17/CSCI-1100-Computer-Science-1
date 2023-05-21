# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:25:47 2019

@author: matth
"""

hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)

if hd > he and he > hs:
    print("Dale")
    print("Erin")
    print("Sam")
elif hd > hs and hs > he:
    print("Dale")
    print("Sam")
    print("Erin")
elif he > hd and hd > hs:
    print("Erin")
    print("Dale")
    print("Sam")
elif he > hs and hs > hd:
    print("Erin")
    print("Sam")
    print("Dale")
elif hs > hd and hd > he:
    print("Sam")
    print("Dale")
    print("Erin")
elif hs > he and he > hd:
    print("Sam")
    print("Erin")
    print("Dale")
    
