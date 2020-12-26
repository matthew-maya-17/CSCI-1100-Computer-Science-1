# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:21:29 2019

@author: matth
"""
"""The objective of this program is to return a couple of statements which show
the result of a gumball selling experiment which we were conducting"""

"""import statement taking the pi and ceil function from the math class"""
from math import pi,ceil

"""The objective of this function is to find the volume of a sphere given the radius"""
def find_volume_sphere(radius):
    volume = (4/3)*pi*(radius**3)
    return volume

"""The objective of this function is to find the volume of a cube given one of the side lengths"""
def find_volume_cube(side):
    volume = side**3
    return volume

#asks and prints a float value that represents what the user would like the gumball radius to be
gumball_radius = input("Enter the gum ball radius (in.) => ")
print(gumball_radius)

#asks and prints an int value that represents what the user would like the weekly sales to be
weekly_sales = int(input("Enter the weekly sales => "))
print(weekly_sales)
print("")

side_capacity_gumballs = (ceil((weekly_sales*1.25)**(1/3)))
gumball_diameter = float(gumball_radius)*2
edge_length = side_capacity_gumballs * gumball_diameter
target_sales = ceil(weekly_sales*1.25)
maximum_occupancy = (side_capacity_gumballs **3) - target_sales
target_wasted_space = (find_volume_cube(edge_length) - find_volume_sphere(float(gumball_radius))*target_sales)
full_wasted_space = find_volume_cube(edge_length)-find_volume_sphere(float(gumball_radius))*side_capacity_gumballs**3

#prints how many gumballs the machine needs to hold along each edge
print("The machine needs to hold " + str(side_capacity_gumballs) + " gum balls along each edge.")
#prints the edge length of the cube
print("Total edge length is {0:.2f} inches.".format(edge_length))
#prints the target sales value and the actual amount the machine holds
print("Target sales were " + str(target_sales)+ ", but the machine will hold " + str(maximum_occupancy) +" extra gum balls.")
#prints the value of wasted space in cubic inches for the target number of gumballs
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(target_wasted_space))
#prints the value of wasted space in cubic inches for the maximum amount of gumballs
print("or {:.2f} cubic inches if you fill up the machine.".format(full_wasted_space))