# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:38:13 2019

@author: matth
"""
""" The objective of this program is to to determine the tone of a sentence
using words which are counted as positive and negative
"""

"""The objective of this function is to determine the number of positive words
in a sentence, which the user will input,
"""
#function which returns the number of positive word contained within the sentence
def number_happy(sentence):
    new_sentence = sentence.lower().replace(" ", "")
    laugh_counter = new_sentence.count("laugh")
    happiness_counter = new_sentence.count("happiness")
    love_counter = new_sentence.count("love")
    excellent_counter = new_sentence.count("excellent")
    good_counter = new_sentence.count("good")
    smile_counter = new_sentence.count("smile")
    return(laugh_counter+happiness_counter+love_counter+excellent_counter+good_counter+smile_counter)

"""The objective of this function is to determine the number of negative words
 in a sentence, which the user will input.
 """
#function which returns the number of negative word contained within the sentence
def number_sad(sentence): 
    new_sentence = sentence.lower().replace(" ", "")
    bad_counter = new_sentence.count("bad")
    sad_counter = new_sentence.count("sad")
    terrible_counter = new_sentence.count("terrible")
    horrible_counter = new_sentence.count("horrible")
    problem_counter = new_sentence.count("problem")
    hate_counter = new_sentence.count("hate")
    return(bad_counter+sad_counter+terrible_counter+horrible_counter+problem_counter+hate_counter)
    
#asks and prints a sentence which the user will use to determine tone of sentence
user_sentence = input("Enter a sentence => ")
print(user_sentence)

#Prints a "+" correlating to the number of positive words contained within the sentence
#and a "-" correlating to the number of negative words contained within the sentence
print("Sentiment: " + "+"*number_happy(user_sentence) + "-"*number_sad(user_sentence))

#if statement to determine the tone of the sentence
if (number_happy(user_sentence) > number_sad(user_sentence)):
    print("This is a happy sentence.")
elif (number_happy(user_sentence) < number_sad(user_sentence)):
    print("This is a sad sentence.")
else:
    print("This is a neutral sentence.")