# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:51:24 2019

@author: matth
"""

def frame_string(frame_string):
    print("*" * 3 + "*" * len(frame_string) + "*" * 3)
    print("*" * 2, frame_string, "*" * 2)
    print("*" * 3 + "*" * len(frame_string) + "*" * 3)

frame_string("Spanish Inquisition")  
print(" ") 
frame_string("Ni") 