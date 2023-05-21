# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:26:20 2019

@author: matth
"""
from Check2_helper import make_square
from PIL import Image ##must import Image first to be able to use it

#image thats being created 
blank_im = Image.new('RGB', (512,512))

make_square("ca.jpg")
make_square("hk.jpg")
make_square("bw.jpg")
make_square("im.jpg")

blank_im.paste(make_square("ca.jpg"), (0,0))
blank_im.paste(make_square("hk.jpg"), (256,0))
blank_im.paste(make_square("bw.jpg"), (256,256))
blank_im.paste(make_square("im.jpg").resize((256,256)), (0,256))

blank_im.show()