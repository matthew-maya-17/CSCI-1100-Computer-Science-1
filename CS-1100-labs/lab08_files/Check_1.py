# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 04:04:45 2019

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
    
print(get_words("(ACM)Association for Computing Machinery|The Rensselaer Student Chapter of the Association for Computing Machinery is RPI's Computer Club. But it's also much more. The RPI-ACM provides a range of services and benefits to its members and to the RPI community."))