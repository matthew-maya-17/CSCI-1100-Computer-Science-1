# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:02:38 2019

@author: matth
"""

def earlier_semester(first_tuple,second_tuple):
    first_season,first_year = first_tuple
    second_season,second_year = second_tuple
    return first_year < second_year or (first_year == second_year and first_season == 'Spring'  and second_season == 'Fall')

w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))