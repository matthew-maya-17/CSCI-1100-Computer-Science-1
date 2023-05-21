# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:53:49 2019

@author: matth
"""

def frame_string(frame_string):
    print("*" * 3 + "*" * len(frame_string) + "*" * 3)
    print("*" * 2, frame_string, "*" * 2)
    print("*" * 3 + "*" * len(frame_string) + "*" * 3)

frame_string("Inquisition")  