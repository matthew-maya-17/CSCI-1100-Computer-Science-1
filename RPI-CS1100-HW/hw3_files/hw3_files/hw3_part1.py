# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:08:44 2019

@author: matth
"""
"""The objective of this program is to return information based on a paragraph
which th user will input"""

"""import statement takes the find_num_syllables function from the syllables class"""
from syllables import find_num_syllables

paragraph = input("Enter a paragraph => " )
print(paragraph)
list_of_words_in_paragraph = paragraph.split() #creates new list for every word

#average sentence length
periods_in_paragraph = paragraph.count(".")
number_of_words_in_paragraph = len(list_of_words_in_paragraph)
ASL = number_of_words_in_paragraph / periods_in_paragraph

#percent hard words
hardword_counter = 0
hard_words = [] #empty list to add hardwords in once they're found
for i in list_of_words_in_paragraph:
    if find_num_syllables(i) >= 3 and not (i.find("-") > 0) : #if statement includes syllables over 3 syllables and words that dont contain a hyphen
        hardword_counter += 1
        hard_words.append(i) #add hardwords in hard_words (empty list)
print("Here are the hard words in this paragraph:")
print(hard_words)
PHW = (hardword_counter/len(list_of_words_in_paragraph))*100

#average number of syllables
sum_syllables = 0
for i in list_of_words_in_paragraph: #runs through every word in the list
    sum_syllables += find_num_syllables(i) #sums up all the syllables in each word in the list
ASYL = sum_syllables/len(list_of_words_in_paragraph)

#GFRI and FKRI variables
GFRI = 0.4*(ASL + PHW)
FKRI = 206.835-1.015*ASL-86.4*ASYL

#print(list_of_word_in_paragraph)
print("Statistics: ASL:{0:.2f} PHW:{1:.2f}% ASYL:{2:.2f}".format(ASL,PHW,ASYL))
print("Readability index (GFRI): {:.2f}".format(GFRI))
print("Readability index (FKRI): {:.2f}".format(FKRI))