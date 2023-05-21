# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:59:01 2019

@author: matth
"""
class Ball(object):
    def __init__(self, x0, y0, dx, dy, r, color):
        
        self.x = x0
        self.y = y0
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color = color
    
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        return (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        if (0 <= self.x - self.r <= maxx and 0 <= self.y - self.r <= maxy) or (0 <= self.x + self.r <= maxx and 0 <= self.y + self.r <= maxy):
            return True
        return False
    
    def check_and_reverse(self, maxx, maxy):
        if 0 >= self.x or self.x >= maxx:
            self.dx *= -1
        if 0 >= self.y or self.y >= maxy:
            self.dy *= -1
            
        return (self.dx, self.dy)