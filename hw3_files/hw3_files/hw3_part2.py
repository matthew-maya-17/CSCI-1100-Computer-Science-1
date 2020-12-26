# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:52:46 2019

@author: matth
"""

"""The objective of this program is to move Pikachu around a board according
to user input like the direction, what type of Pokemon to fight"""

"""The objective of this function is to return a tuple with the row and column location of pikachu"""
def move_pokemon(original_location, direction, steps):
    row,column = original_location 
    #sets boundaries of square(150x150)
    if row > 150:
        row = 150
    elif column > 150:
        column = 150
    elif column < 0:
        column = 0
    elif row < 0:
        row = 0
    #if direction equals north then subtract number of steps from row
    if direction.lower() == "n":
        new_tuple = (row - steps,column) 
    #if direction equals east then add number of steps from column
    elif direction.lower() == "e":
        new_tuple = (row,column + steps)
    #if direction equals south then  number of steps from rows
    elif direction.lower() == "s":
        new_tuple = (row + steps,column)
    #if direction equals west then subtract number of steps from column
    elif  direction.lower() == "w":
        new_tuple = (row,column - steps)
    else:
        new_tuple = (row, column)
    return new_tuple

#Variables asking for user input and storing that value/string
turns = int(input("How many turns? => "))
print(turns)
pikachu_name = input("What is the name of your pikachu? => " )
print(pikachu_name)
often = int(input("How often do we see a Pokemon (turns)? => "))
print(often)

#new_row,new_column = move_pokemon((75,75), 'N', 5)
newer_tuple = (75,75)
new_row,new_column = newer_tuple

record_list = [] #empty list which will grow as Pikachu faces other opponents
turn_counter = 0
#original turn and location
print("\nStarting simulation, turn 0 {} at (75, 75)".format(pikachu_name))
while turn_counter < turns: #while user the turncounter is less than the user input of turns keep running
    #Variables asking the user for a direction to input
    direction = input("What direction does {} walk? => ".format(pikachu_name))
    print(direction)
    
    #replaces old tuple with a new location for row and column
    newer_tuple = (new_row,new_column)
    new_row,new_column = move_pokemon((newer_tuple), direction, 5)

    turn_counter += 1
    if turn_counter % often == 0: #if the count is divisible by variable input ask user what pokemon he meets
        print("Turn {0:}, {1:} at {2:}".format(turn_counter,pikachu_name, newer_tuple))
        pokemon_met = str(input("What type of pokemon do you meet (W)ater, (G)round? => "))
        print(pokemon_met)
        #the following if statement saves your status against another pokemon and updates location of your pikachu (lines 70-83)
        if pokemon_met.lower() == "g":
#            if direction.lower() == "n":
#                
#            elif direction.lower() == "s":
#                move_pokemon((75,75), (row - steps,column), 10)
            #enter tuple for direction 10 steps in opposite direction it came from
            print("{0:} runs away to {1:}".format(pikachu_name,(75,75)))#need to enter tuple
            record_list.append('Lose')
        elif pokemon_met.lower() == "w":
            move_pokemon((newer_tuple), direction, 1)
            print("{} wins and moves to {}".format(pikachu_name,move_pokemon((75,75), direction, 1)))#need to enter tuple
            record_list.append('win')
        else:
            record_list.append('No Pokemon')
    newer_tuple = (new_row,new_column)
newer_tuple = (new_row,new_column)

#prints final information about your pikachu
print("{0:} ends up at {1:}, Record: {2:}".format(pikachu_name,newer_tuple,record_list))