# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:08:33 2019

@author: matth
"""

"""The objective of this program is to ask the user to input a title which will be reference from a Harry Potter
movie to see if the title which they entered is contained in order to spit out the monsters which were featured in
the movie. The objective of this program is to also print all other titles that have at least one beast in common 
with this title in lexicographical order and Print all the beasts that were featured only in the selected title. 
The program will run until the user enters stop for the title."""
import textwrap

title = ""
movies = []

#creates a list of lists which contains the title of the harry potter movies along with a set of monsters contained in the movie
for line in open("titles.txt"):
    movie_description = line.strip("\n").split("|")
    movies.append([movie_description[0], set(movie_description[1:])])

#user input for a title
title = str(input("Enter a title (stop to end) => "))
print(title)
print('')
#while loop which will continue until the user types stop
while title.strip().lower() != "stop":
    #variables
    similar_titles = []
    index_found = ''
    print_string = ''
    exists = False
    

    for film in movies:
        if title.lower() in film[0].lower():
            index_found = movies.index(film)
            exists = True
            break
    if exists != True:
        print('This title is not found!\n')
    elif exists == True:
        print('Found the following title:', movies[index_found][0])
        beasts_in_title = movies[index_found][1]
        for i in sorted(beasts_in_title):
            print_string = print_string + i + ', '
        print_string = 'Beasts in this title: ' + print_string[:-2]
        lines = textwrap.wrap(print_string)
        for i in lines:
            print(i)
        print('')
        print_string = ''
        
        #compare with other movies character sets to find similar movies
        for film in movies:
            if movies[index_found][1] & film[1] != set():
                similar_titles.append(film[0])
        similar_titles.sort()
        similar_titles.remove(movies[index_found][0])
        for i in similar_titles:
            print_string = print_string + i + ', '
        print_string = 'Other titles containing beasts in common: ' + print_string[:-2]
        lines = textwrap.wrap(print_string)
        for words in lines:
            print(words)
        print('')
        print_string = ''
        
                #Use set subtraction to find unique characters
        for film in movies:
            if film == movies[index_found]:
                pass
            else:
                beasts_in_title = beasts_in_title - film[1]
        beasts_in_title = sorted(list(beasts_in_title))
        for beast in beasts_in_title:
            print_string = print_string + beast + ', '
        print_string = 'Beasts appearing only in this title: ' + print_string[:-2]
        lines = textwrap.wrap(print_string)
        for word in lines:
            print(word)
        print('')
        
    title = str(input("Enter a title (stop to end) => "))
    print(title)
    print('') 