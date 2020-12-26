# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:50:48 2019

@author: matth
"""
#Mad Libs HW (HW #1)

#intro Speech to Mad Libs
print("Let's play Mad Libs for Homework 1 \nType one word responses to the following:\n")

name = input('proper_name ==> ')
print(name)
adjective_1 = input('adjective ==> ') 
print(adjective_1)
noun_1 = input('noun ==> ')
print(noun_1)
verb_1 = input('verb ==> ') 
print(verb_1)
verb_2 = input('verb ==> ') 
print(verb_2)
noun_2 = input('noun ==> ')
print(noun_2)
emotion_1 = input('emotion ==> ')
print(emotion_1)
verb_3 = input('verb ==> ') 
print(verb_3)
noun_3 = input('noun ==> ')
print(noun_3)
season = input('season ==> ') 
print(season)
adjective_2 = input('adjective ==> ') 
print(adjective_2)
emotion_2 = input('emotion ==> ')
print(emotion_2)
team_name = input('team-name ==> ')
print(team_name)
noun_4 = input('noun ==> ')
print(noun_4)
adjective_3 = input('adjective ==> ') 
print(adjective_3 + "\n")

print("Here is your Mad Lib...")
print("")
print("Good morning", name + "!\n")
print("\tThis will be a/an", adjective_1 + " " + noun_1 +"! Are you", verb_1, "forward to it?")
print("\tYou will", verb_2,"a lot of", noun_2, "and feel", emotion_1, "when you do. \n\tIf you do not, you will", verb_3,"this", noun_3 +".\n")
print("\tThis",season,"was",adjective_2+". Were you",emotion_2,"when",team_name,"won\n\tthe",noun_4 + "?\n")
print("\tHave a/an",adjective_3, "day!")