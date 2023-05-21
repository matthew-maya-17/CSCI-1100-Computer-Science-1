# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:08:44 2019

@author: matth
"""
from PIL import Image 

def make_square(image_object):
    image = Image.open(image_object)
    w,h = image.size
    if w > h:
        image.crop((0,0,w,w))
        return image
    else:
        image.crop((0,0,h,h))
        return image
