# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:30:40 2019

@author: matth
"""

def find_min(LIST):
    min_list_in_each_index = []
    for i in range(len(LIST)):
        min_list_in_each_index.append(min(LIST[i]))
        real_min = min(min_list_in_each_index)
    return real_min
    
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )