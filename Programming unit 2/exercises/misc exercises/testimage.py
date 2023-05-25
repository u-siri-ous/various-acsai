# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:59:36 2021

@author: Siria
"""
import images 

im = [[(0,0,0)] * 400 for _ in range(300)]
images.save(im, 'test.png')