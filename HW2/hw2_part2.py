# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:54:41 2019

@author: matth
"""
"""The objective of this program is to ask the user for a message to encyrpt
 and decrypt the encrypted message to see if it is reversible or not"""

"""The objective of this function is to encrypt a message which the user will enter"""
def encrypt(word) :
    new_word = word.replace(' a','%4%').replace('he','7!').replace('e','9(*9(').replace('y','*%$').replace('u','@@@').replace('an','-?').replace('th','!@+3').replace('o','7654').replace('9','2').replace('ck','%4')
    return new_word
    
"""The objective of this function is to decrypt a message which will be taken in as an arguement"""
def decrypt(word):
    new_word = word.replace('%4','ck').replace('%4%',' a').replace('7!','he').replace('2','9').replace('9(*9(','e').replace('*%$','y').replace('@@@','u').replace('-?','an').replace('!@+3','th').replace('7654','o')
    return new_word

#asks and prints a word which the user will use to encrypt and dycrpt
user_word = input("Enter a string to encode ==> ")
print(user_word + "\n")

#print statement showing the result of the encrypted message which the user inputs
print("Encrypted as ==> " + encrypt(user_word))

#prints the difference in length between the orginal message and the encrypted message
print("Difference in length ==> " + str(len(encrypt(user_word)) - len(user_word)))

#print statement showing the result of the decrypted message which the encrypt function spits out
print("Deciphered as ==> " + decrypt(encrypt(user_word)))

#if statement which prints out whether the original message, which the user input, is reversible or not
if decrypt(encrypt(user_word)) == user_word:
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")
