# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:55:39 2019

@author: matth
"""

#bpop = int(input("Number of bunnies ==> "))
#print(bpop)
#fpop = int(input("Number of foxes ==> "))
#print(fpop)
#bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
#fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
#print("Year 1:" + str(bpop) + " " + str(fpop))
#print("Year 2: " + str(bpop_next)+ " "+ str(fpop_next))

def pop(bpop,fpop):
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    print("Year 1:" + str(bpop) + " " + str(fpop))
    print("Year 2: " + str(bpop_next)+ " "+ str(fpop_next))
    bpop = bpop_next
    fpop = fpop_next
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    print("Year 3: " + str(bpop_next*bpop_next)+ " "+ str(fpop_next))
    bpop = bpop_next
    fpop = fpop_next
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    print("Year 4: " + str(bpop_next)+ " "+ str(fpop_next))
    bpop = bpop_next
    fpop = fpop_next
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    print("Year 5: " + str(bpop_next)+ " "+ str(fpop_next))
#    bpop_next_next = int((10*bpop_next)/(1+0.1*bpop_next) - 0.05*bpop_next*fpop_next)
#    fpop_next_next = int(0.4 * fpop_next + 0.02 * fpop_next * bpop_next)
#    print("Year 3: " + str(bpop_next_next)+ " "+ str(fpop_next_next))
#    bpop_next_next_next = int((10*bpop_next_next)/(1+0.1*bpop_next_next) - 0.05*bpop_next_next*fpop_next_next)
#    fpop_next_next_next = int(0.4 * fpop_next_next + 0.02 * fpop_next_next * bpop_next_next)
#    print("Year 4: " + str(bpop_next_next_next) + " " + str(fpop_next_next_next))
#    bpop_next_next_next_next = int((10*bpop_next_next_next)/(1+0.1*bpop_next_next_next) - 0.05*bpop_next_next_next*fpop_next_next_next)
#    fpop_next_next_next_next = int(0.4 * fpop_next_next_next + 0.02 * fpop_next_next_next * bpop_next_next_next)
#    print("Year 5: " + str(bpop_next_next_next_next) + " " + str(fpop_next_next_next_next))
    
pop(100,10)
    