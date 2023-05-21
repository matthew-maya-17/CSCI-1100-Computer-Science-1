# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 01:22:03 2019

@author: matth
"""

from PIL import Image ##must import Image first to be able to use it

#image thats being created 
blank_im = Image.new('RGB', (512,512))

im = Image.open("im.jpg")
im = im.resize((256,256)) # resize to the given width/height passed as a tuple
ca = Image.open("ca.jpg")
ca = ca.resize((256,256)) # resize to the given width/height passed as a tuple
hk = Image.open("hk.jpg")
hk = hk.resize((256,256)) # resize to the given width/height passed as a tuple
bw = Image.open("bw.jpg")
bw = bw.resize((256,256)) # resize to the given width/height passed as a tuple

blank_im.paste(im, (0,0))
blank_im.paste(ca, (256,0))
blank_im.paste(hk, (256,256))
blank_im.paste(bw, (0,256))

blank_im.show()