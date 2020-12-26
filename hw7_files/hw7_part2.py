# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 02:36:43 2019

@author: matth
"""
"""The objective of this program is to ask the user for a genre and return the best and worst movie, between 
the input values minimum year and maxiumum year, along with a description stating when the movie was released 
and the average rating for the movie. """

import json
if __name__ == "__main__":
    #reads the json files
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    #user input variables
    minimum_year = int(input("Min year => ").strip(" "))
    print(minimum_year)
    maximum_year = int(input("Max year => ").strip(" "))
    print(maximum_year)
    IMDB_weight = input("Weight for IMDB => ").strip(" ")
    print(IMDB_weight)
    IMDB_weight = float(IMDB_weight)
    twitter_weight = float(input("Weight for Twitter => ").strip(" "))
    print(twitter_weight)
    twitter_weight = float(twitter_weight)
    print("")
    genre = ''
    
    #list and dictionaries to store values
    movies_selected = dict()
    movies_to_remove = []
   
    for ID in movies:
        if movies[ID]['movie_year'] >= minimum_year and movies[ID]['movie_year'] <= maximum_year:
            movies_selected[ID] = movies[ID]
    for movie in movies_selected:
        if movie in ratings:
            if len(ratings[movie]) >= 3:
                rating = (IMDB_weight* movies_selected[movie]['rating'] + twitter_weight * sum(ratings[movie])/len(ratings[movie]))/(IMDB_weight+twitter_weight)
                movies_selected[movie]['rating'] = rating
            else:
                movies_to_remove.append(movie)
        else:
            movies_to_remove.append(movie)
    for i in movies_to_remove:
        movies_selected.pop(i)
    genre = input('What genre do you want to see? ')
    print(genre)
    genre = genre.lower().strip()
    print("")
    #while loop which will continue until the user types stop
    while genre != 'stop':
        genre_movies = []
        for movie in movies_selected:
            for j in movies_selected[movie]['genre']:
                if j.lower() == genre:
                    genre_movies.append((movies_selected[movie]['rating'], movies_selected[movie]['name'], movies_selected[movie]))
        genre_movies = sorted(genre_movies, reverse = True)
        if genre_movies != []:
            print('Best:\n\tReleased in ', genre_movies[0][2]['movie_year'], ', ', genre_movies[0][1], ' has a rating of {:.2f}'.format(genre_movies[0][0]), '\n', sep='')
            print('Worst:\n\tReleased in ', genre_movies[-1][2]['movie_year'], ', ', genre_movies[-1][1], ' has a rating of {:.2f}'.format(genre_movies[-1][0]), '\n', sep='')
        else:
            print('No ', genre.title(), ' movie found in ', minimum_year, ' through ', maximum_year, '\n', sep = '')
        genre = input('What genre do you want to see? ')
        print(genre)
        genre = genre.lower().strip()
        if genre == 'stop':
            break
        print()