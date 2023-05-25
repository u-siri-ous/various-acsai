# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:00:27 2021

@author: Siria

Write a function that takes as input an image, a row, a column, a color, a length and an 
height and draws a rectangle with upper-left corner in row-column, of size lengthxheight 
and filled with color.

"""
import images
from math import sqrt

im = [[(0,0,0)] * 400 for _ in range(400)] #background

def rect(im, row, col, width, height, color):
   for y in range(row, row + width):
      for x in range(col, col + height):
         im[y][x] = color
         

