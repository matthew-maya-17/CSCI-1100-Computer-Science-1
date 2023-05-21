# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:59:09 2019

@author: matth
"""


bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def ok_to_add(r, c, value):
    if r < 0 or r >= len(bd) or c < 0 or c >= len(bd[r]):
        return False
    original = bd[r][c]
    bd[r][c] = '.'

    # check row
    for i in range(len(bd[r])):
        if bd[r][i] == value:
            bd[r][c] = original
            return False

    # check col
    for p in range(len(bd[0])):
        if bd[p][c] == value:
            bd[r][c] = original
            return False


    # check diagonal
    start_row = r - (r%3);
    start_col = c - (c%3);

    for a in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if bd[a][j] == value:
                bd[r][c] = original
                return False

    bd[r][c] = value
    return True

for i in range(len(bd)):
    if i == 0 or i == 3 or i == 6 or i == 9:
        print("-------------------------")
    for p in range(len(bd[i])):
        if  p == 0 or p == 3 or p == 6 or p == 9:
            print("|", end = " ")
        print(bd[i][p], end = " ")
        if p == len(bd[i])-1:
            print("|")
print("-------------------------")
print(ok_to_add(5,1,"7"))