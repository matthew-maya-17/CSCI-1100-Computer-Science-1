# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:18:48 2019

@author: matth
"""
#original number values and inputs
frame_character= input('Enter frame character ==> ')
print(frame_character)
box_height = input('Height of box ==> ') 
print(box_height)
box_height = int(box_height)
box_width = input('Width of box ==> ')
print(box_width + "\n")
box_width = int(box_width)


#equations and new variables
dimension = str(box_width) + "x" + str(box_height)
edge = (frame_character + " " * ((box_width) - 2) + frame_character)
number_before_dimension = int((round(((box_height - 2)/2),0) - 1))
number_after_dimension = int(((box_height - 2)/2))
blank_spaces_before_dimension = int((((box_width - 2) - len(dimension))/2))
blank_spaces_after_dimension = int(round((((box_width - 2) - len(dimension))/2) + 0.5,0))


#print statements executing code
print("Box:")
print(frame_character * box_width)
print((edge + "\n")* number_before_dimension, end='')
#print((edge + "\n") * (box_height - 2), end='')
print(frame_character + " " * blank_spaces_before_dimension + str(box_width) + "x" + str(box_height)+ " " * blank_spaces_after_dimension+ frame_character)
print((edge + "\n") * number_after_dimension, end='')
print(frame_character * box_width)
#print(frame_character + " " * ((box_width) - 2) + frame_character)
#print((frame_character + "\n") * (box_height - 1))
#print(frame_character * (box_width - 1))
#print(frame_character * 2, box_height + "x" +  * (x-len(first_name)) + frame_character * 2)