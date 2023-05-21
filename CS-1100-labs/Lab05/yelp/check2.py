# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:45:11 2019

@author: matth
"""
import lab05_util

index = int(input("Enter id of a restaurant: " ))
def print_info(restaurant):
#        restaurants[index]
        print(restaurant[0])
        
        location = restaurant[3].split("+")
        print("\t" + "\n\t".join(location))
        total = 0
        
        for i in restaurant[6] :
            total += i
        count= len(restaurant[6])
        avg =(total)/len(restaurant[6])
        if avg > 0 and avg < 2:
            print("This restaurant is rated bad, based on {} reviews.".format(count))
        elif avg > 2 and avg < 3:
            print("This restaurant is rated average, based on {} reviews.".format(count))
        elif avg > 3 and avg < 4:
            print("This restaurant is rated bad, based on {} reviews.".format(count))
        elif avg > 4 and avg < 5:
            print("This restaurant is rated average, based on {} reviews.".format(count))

####### main code starts here
restaurants = lab05_util.read_yelp('yelp.txt')
if index > len(restaurants):
    print("Warning too high!")
else:
    print_info(restaurants[index-1])