# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:31 2019

@author: matth
"""

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
 
"""The objective of this function is to return the # of turns and the resulting grid""" 
def run_one_simulation(grid, prob):
    turn = 0
    false = 3
    true = 1
    p = float(prob)
    pokemon_seen = 0
    pokemon_caught = 0    
    row,column = (size//2, size//2) #variable which breaks the starting location into row and column
    
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
            pokemon_seen += 1
            if throw_pokeball(false, true) == True:
                true += 1 
                pokemon_caught += 1
                grid[row][column] += 1
            else:
                grid[row][column] -= 1
    return(grid, turn)
    
if __name__ == "__main__":
    #user input
    size = int(input("Enter the integer grid size => "))
    print(size)
    p = input("Enter a probability (0.0 - 1.0) => ")
    print(p)
    p = float(p)
    runs = int(input("Enter the number of simulations to run => "))
    print(runs,'\n', sep='')
    
    list_turns= []
    grid_count = []
    total_turns = []
    for i in range(size):
        grid_count.append([0] * size)
    
    #Set initial seed
    seed_value = 10 * size + size
    random.seed(seed_value)
    simulation = 0
    
    #Run the simulations
    while simulation < runs:
        this_sim = run_one_simulation(grid_count, p)
        grid_count = this_sim[0]
        list_turns.append(this_sim[1])
        simulation += 1
        
    #Print the grid
    for i in range(0, len(grid_count)):
        for j in range(0, len(grid_count[i])):
            print(' '*(4-len(str(grid_count[i][j]))), grid_count[i][j], end='')
        print('\n', end='')
        
    #Create a list from all the lists in the grid list.
    for i in grid_count:
        for j in i:
            total_turns.append(j)

#final print statements with the statistics
print("Average number of turns in a simulation was {:.2f}".format(sum(list_turns)/len(list_turns)))
print("Maximum number of turns was {0:} in simulation {1:}".format(max(list_turns), list_turns.index(max(list_turns)) + 1))
print("Minimum number of turns was {0:} in simulation {1:}".format(min(list_turns), list_turns.index(min(list_turns)) + 1))
print('Best net missed pokemon versus caught pokemon is', max(total_turns))
print('Worst net missed pokemon versus caught pokemon is', min(total_turns))