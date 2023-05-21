# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:36:08 2019

@author: matth
"""
def get_words(file):
    words = set()
    for line in open(file):
        curr = line.strip().split('|')
        des = curr[1].replace(","," ")
        des = des.replace("."," ")
        des = des.replace("("," ")
        des = des.replace(")"," ")
        des = des.replace("/"," ")
        curr = des.split(" ")
        for i in curr:
            i.lower()
            if i.isalpha() and len(i)>=4:
                word = i.strip()
                words.add(word)
    return words

def get_words2(string):
    words = set()
   
    curr = string.strip().split('|')
    des = curr[1].replace(","," ")
    des = des.replace("."," ")
    des = des.replace("("," ")
    des = des.replace(")"," ")
    des = des.replace("/"," ")
    curr = des.split(" ")
    for i in curr:
        i.lower()
        if i.isalpha() and len(i)>=4:
            word = i.strip()
            words.add(word)
    return words

file1 = input("Enter file name: ").strip()
print(file1)

file2 = input("Enter file name of all clubs: ").strip()
print(file2)

w1 = get_words(file1)

def sim(w1,w2):
    common = set()
    for i in w1:
        if i in w2:
            common.add(i)
    sim = len(common)
    return sim

l5 = []
for line in open(file2):
    curr = line.strip().split('|')
    word2 = get_words2(line)
    name = curr[0]

    sim1 = sim(w1,word2)
    c = (sim1,name)
    l5.append(c)
   

#print(l5)
l5.sort(reverse = True)
print(l5[0][1],l5[1][1],l5[2][1],l5[3][1],l5[4][1])