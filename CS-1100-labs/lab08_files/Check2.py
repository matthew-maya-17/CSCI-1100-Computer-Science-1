# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:15:28 2019

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

s1 = get_words("WRPI|WRPI is the campus radio station. We broadcast 365 days a year at 10,000 effective watts for up to 75 miles around RPI. Our studios are located on the first floor of the DCC. Our programming includes a wide range of alternative and experimental music, cultural and public affairs programs, live local bands, special events, and sports simulcasts.")
print(s1)
s2 = get_words("Chinese American Students Association|The Chinese American Students Association is a group of students from various geographical areas gathering to advance friendship and pride amongst the members. This organization brings out all aspects and presents the Chinese culture to the Rensselaer community through various events which include Chinese Cultural festivals, movies, and social gatherings. The Chinese American Students Association welcomes new students to the Rensselaer community and helps them adjust to life at Rensselaer.")
print(s2)
s3 = s1.intersection(s2)
print(s3)
