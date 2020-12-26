# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:27:04 2019

@author: matth
"""

"""The objective of this program is to use the functions from part 1 to see if the pokemon trainer runs
into a pokemon and to see if he is able to catch a pokemon depending on the user probabilty"""
import random

"""The objective of this function is to return a random a tuple which contains
a direction and a random value"""
def move_trainer():
    directions =  ['N', 'E', 'S', 'W']
    direction = random.choice(directions)
    seen = random.random()
    return (direction, seen)

"""The objective of this function is to return a random boolean statement that is contained in
a list which is made up from the parameters which the function takes in"""
def throw_pokeball(num_false, num_true):
    boolean_list = []
    for i in range(num_false):
        boolean_list.append(False)
    for i in range(num_true):
        boolean_list.append(True)
    return(random.choice(boolean_list))
    
if __name__ == "__main__":
    """assigned variables"""
    turn = 0
    false = 3
    true = 1
    pokemon_seen = 0
    pokemon_caught = 0
    
    """user variables"""
    size = int(input("Enter the integer grid size => "))
    print(size)
    p = input("Enter a probability (0.0 - 1.0) => ")
    print(p)
    p = float(p)
    
    #seed
    seed_value = 10 * size + size
    random.seed(seed_value)
    
    #variable which breaks the starting location into row and column
    row,column = (size//2, size//2)
    
    """while loop which runs until either the row or column hits 0 or goes above size-1"""
    while (row > 0 and row < size - 1) and (column > 0 and column < size - 1):
        turn += 1
        compass_direction, seen = move_trainer() 
        if compass_direction == 'N':
            location = (row-1,column)
        if compass_direction == 'S':
            location = (row+1,column)
        if compass_direction == 'E':
            location = (row,column+1)
        if compass_direction == 'W':
            location = (row,column-1)
        row,column = location
        """if value is less than user input  then report seeing a pokemon and throw 
        pokeball to see if the trainer is able to catch the pokemon at the specified turn"""
        if seen <= p:
            print("Saw a pokemon at turn {}, location {}".format(turn,location))
            pokemon_seen += 1
            if throw_pokeball(false, true) == True:
                print('Caught it!')
                true += 1 
                pokemon_caught += 1
            else:
                print('Missed ...')
    """print statement which concludes where the trainer ended up after a number of terms, 
    how many pokemon were seen and how many pokemon were successfully caught"""
    print('Trainer left the field at turn ', turn, ', location ', (row,column), '.\n', pokemon_seen, \
' pokemon were seen, ', pokemon_caught, ' of which were captured.', sep='')