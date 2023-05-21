# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:36:35 2019

@author: matth
"""

import lab05_util
def print_info(restaurant):
    print(restaurant[0])
    location = restaurant[3].split("+")
    print("\t" + "\n\t".join(location))
    total = 0
    for i in restaurant[6] :
        total += i
    print("Average Score : {:.2f}".format((total)/len(restaurant[6])))

####### main code starts here
restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])