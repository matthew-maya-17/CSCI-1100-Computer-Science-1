# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:31:08 2019

@author: matth
"""
"""The objective of this program is to set up the functions move_trainer() and throw_pokeball(num_false, num_true)
for part 2 and 3. In this program you will use randomness to pick a direction, a value, and a boolean statement"""
import random

"""The objective of this function is to print out a list of compass directions and randomly select a direction
and a value from 0-1"""
def move_trainer():
    directions =  ['N', 'E', 'S', 'W']
    print("Directions: {}".format(directions))
    print("Selected {0:}, value {1:.2f}".format(random.choice(directions),random.random()))

"""The objective of this function is to create a list of boolean statement from the parameters 
which are taken in"""
def throw_pokeball(num_false, num_true):
    boolean_list = []
    for i in range(num_false):
        boolean_list.append(False)
    for i in range(num_true):
        boolean_list.append(True)
    print("Booleans: {}".format(boolean_list))
    print("Selected ", random.choice(boolean_list),sep = "")
    
if __name__ == "__main__":
    #the following variables are all user input which are used for the functions
    size = int(input("Enter the integer grid size => "))
    print(size)
    false = int(input("Enter the integer number of Falses => "))
    print(false)
    true = int(input("Enter the integer number of Trues => "))
    print(true)
    
    #seed
    seed = 11 * size
    random.seed(seed)
    print("Setting seed to {}".format(seed))
    
    #allows for the function to run 5 times
    for i in range(5):
        move_trainer()
    for i in range(5):
        throw_pokeball(false, true)