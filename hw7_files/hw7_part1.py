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
a list of words conatined in a dictionary. Each step will return a tuple which will be used in the final print statement to 
determine what occured in order to see if the word was eligible"""
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def autocorrect(word, dictionary, keyboard):
    possibilities = []
    possibilities_sorted = []
    
    if word in dictionary:
        return [('FOUND', word)]
    #drop
    for letter_index in range(len(word)):
        word_possibility = word[0:letter_index] + word[letter_index+1:len(word)]
        if word_possibility in dictionary and word_possibility not in possibilities:
            possibilities.append(word_possibility)
    #swap
    for letter_index in range(len(word)-1):
        word_option = word[0:letter_index] + word[letter_index+1] + word[letter_index] + word[letter_index+2:len(word)]
        if word_option in dictionary and word_option not in possibilities:
            possibilities.append(word_option)
    #insert            
    for letter_index in range(len(word)+1):
        for letter in alphabet:
            possible_word = word[0:letter_index] + letter + word[letter_index:len(word)+1]
            if possible_word in dictionary and possible_word not in possibilities:
                possibilities.append(possible_word)
    #replace
    for letter_index in range(len(word)):
        for key in keyboard.keys():
            if word[letter_index] ==  key:
                for value in keyboard[key]:
                    possible_replacement = word[0:letter_index] + value + word[letter_index+1:len(word)]
                    if possible_replacement in dictionary and possible_replacement not in possibilities:
                        possibilities.append(possible_replacement)
    if possibilities != []:
        for word in possibilities:
            if (dictionary[word], word) not in possibilities_sorted:
                possibilities_sorted.append((dictionary[word], word))
        possibilities_sorted = sorted(possibilities_sorted, reverse = True)
        for index in range(len(possibilities_sorted)):
            possibilities_sorted[index] = ('MATCH ' + str(index+1), possibilities_sorted[index][1])
        if len(possibilities_sorted) > 3:
            possibilities_sorted = possibilities_sorted[0:3]
        return possibilities_sorted
    return[('NO MATCH', word)]
  
if __name__ == '__main__':
    #user input values which take in a string that will represent a file
    dict_file = str(input("Dictionary file => ")).strip()
    print(dict_file)
    input_file = str(input("Input file => ")).strip()
    print(input_file)
    keyboard_file = str(input("Keyboard file => ")).strip()
    print(keyboard_file)   
    
    words = []
    vocab_dict = dict()
    possible_letters = dict()
      
#adds the words from the text which the user chose to input into a list
    for word in open(input_file, encoding = "ISO-8859-1"):
        words.append(word.strip('\n').strip())
#seperates the lines from dict_file into a list where index 0 is the word and index 1 is the frequency those two
#indices are later used in their respective place to represent the keys and the values in the dictionary vocab_dict
    for line in open(dict_file, encoding = "ISO-8859-1"):
        reference = line.strip('\n').split(',')
        vocab_dict[reference[0]] = reference[1]
#seperates the lines from keyboard_file into a list where index 0 is the the key pressed and index 1 is the surrounding letter
#indices are later used in their respective place to represent the keys and the values in the dictionary possible_letters
    for letters in open(keyboard_file, encoding = "ISO-8859-1"):
        substitutes = letters.strip('\n').split(' ')
        possible_letters[substitutes[0]] = substitutes[1:len(letters)]
        #possible_letters[substitutes[0]] = substitutes[1:len(substitutes)]
              
#runs through every term in the list term to see what autocorrect will spit out        
    for term in words:
        result = autocorrect(term, vocab_dict,possible_letters) 
        for LIST in result:
            print("{0:15s} -> {1:15s} :{2:}".format(term,LIST[1],LIST[0]))
