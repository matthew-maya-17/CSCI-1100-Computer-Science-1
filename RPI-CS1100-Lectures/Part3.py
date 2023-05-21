# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:08:35 2019

@author: matth
"""
base10size = input("Disk size in GB => ")
base10size = int(base10size)
base2size = int((base10size * (10**9))/(2**30))
lost_size = base10size - base2size
print(base10size)
print (base10size, "GB in base 10 is actually", base2size, "GB in base 2,", lost_size, "GB less than advertised.")
print("Input: ", "*"*base10size )
print("Actual:", "*"*base2size )