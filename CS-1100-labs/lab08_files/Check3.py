# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:11:32 2019

@author: matth
"""

def get_words(club):
    unique_words = set()
    club_info = club.split("|")
    club_description = club_info[1]
    club_description = club_description.replace(",", " ")
    club_description = club_description.replace(".", " ")
    club_description = club_description.replace("(", " ")
    club_description = club_description.replace(")", " ")
    club_description = club_description.replace("\"", " ")
    club_description = club_description.lower()
    description_seperated = club_description.split(" ")
    
    for word in description_seperated:
        if word.isalpha() and len(word) >= 4:
            unique_words.add(word)
        else:
            continue
    return unique_words

club1 = get_words("Wrestling|Competitive wrestling in the NCWA. NCAA style wrestling practices daily and competes often.")
for line in open(allclubs.txt):
    line = f.readline()
    
s2 = get_words("Chinese American Students Association|The Chinese American Students Association is a group of students from various geographical areas gathering to advance friendship and pride amongst the members. This organization brings out all aspects and presents the Chinese culture to the Rensselaer community through various events which include Chinese Cultural festivals, movies, and social gatherings. The Chinese American Students Association welcomes new students to the Rensselaer community and helps them adjust to life at Rensselaer.")
s3 = club1.intersection(club2)
print("Same words: {}".format(s3))
print("Unique to wrpi: {}".format(club1))
print("Unique to csa: {}".format(s2))