# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:23:27 2022

@author: lingt
"""
from PIL import Image
image = Image.open("earth2.png")
image = image.resize((1200,300),Image.ANTIALIAS)
image.save(fp="earth.png")