# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:12:08 2019

@author: matth
"""
"""The objective of this program is to create a modified version of autocorrect using
sets to determine if a word is contained in a dictionary otherwise the program can drop a letter 
to see if a word can be made, replace a letter to see if a word can be made or swap two consecutive letters in order
to create a word, otherwise the word is not a match based on the dictionary."""

"""The objective of this function is to create the rules and steps which will compare a word to 
a set of words conatined in a dictionary. Each step will return a tuple which will be used in the final print statement to 
determine what occured in order to see if the word was eligible"""
def autocorrect(word, dictionary_set):
    
    possibilities = []
    
    if word in dictionary_set: #
        return (word, 'FOUND')
    
    for letter_index in range(len(word)):
        word_possibility = word[0:letter_index] + word[letter_index+1:len(word)]
        if word_possibility in dictionary_set:
            possibilities.append(word_possibility)
    if possibilities != []:
        return (min(possibilities), 'DROP')
    
    for letter_index in range(len(word)-1):
        word_option = "";
        word_option = word[0:letter_index] + word[letter_index+1] + word[letter_index] + word[letter_index+2:len(word)]
        if word_option in dictionary_set:
            return (word_option,'SWAP')
    if possibilities != []:
        return (min(possibilities), 'REPLACE',)
    
    alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(word)):
        for j in alphabet:
            w = word[0:i] + j + word[i+1:len(word)]
            if w in dictionary_set:
                possibilities.append(w)
    if possibilities != []:
        return (min(possibilities),'REPLACE')
    return(word, 'NO MATCH')
    
    
if __name__ == '__main__':
    #user input values which take in a string that will represent a file
    dict_file = str(input("Dictionary file => ")).strip()
    print(dict_file)
    input_file = str(input("Input file => ")).strip()
    print(input_file)
    
    words = []
    dict_set = set() #empty set which will include all the words of the dictionary file
    
    #adds the words from the text which the user chose to input into a list
    for word in open(input_file, encoding = "ISO-8859-1"):
        words.append(word.strip('\n'))
    #adds the words from the text which the user chose to use as a dictionary into a list
    for line in open(dict_file, encoding = "ISO-8859-1"):
        dict_set.add(line.strip('\n'))
        
    #runs through every term in the list term to see what autocorrect will spit out    
    for term in words:
        result,word = autocorrect(term, dict_set)
        print("{:15s} -> {:15s} :{:}".format(term,result,word))