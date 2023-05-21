# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:48:35 2019

@author: matth
"""
from Check2_helper import make_square
from PIL import Image

blank_im = Image.new('RGB', (1000,360))

im = Image.open("im.jpg")
w1,h1 = im.size
ca = Image.open("ca.jpg")
w2,h2 = im.size
hk = Image.open("hk.jpg")
w3,h3 = im.size
bw = Image.open("bw.jpg")
w4,h4 = im.size


blank_im.paste(im.resize((int((w1/h1) * 256),256)), (31,20))
blank_im.paste(ca.resize((int((w2/h2) * 256),256)), (297,64))
blank_im.paste(hk.resize((int((w3/h3) * 256),256)), (563,20))
blank_im.paste(bw.resize((int((w2/h2) * 256),256)), (829,64))

blank_im.show()

make_square("ca.jpg")