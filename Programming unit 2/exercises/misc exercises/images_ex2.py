# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:29:01 2021

@author: Siria

Write a function that gets an image file with an image
with black bakground and some white lines not overlapping
or intersecting and a pixel and returns the length of the
white line that passes through that pixel

image corners:
    im[0][0] in alto a sinistra
    im[len(im)-1][len(im[0])-1] in basso a destra
"""
import images

#im = [(0,0,0) * 400 for _ in range(300)]

class Pixel: 
    
    white = (255,255,255)
    black = (0,0,0)
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

def count_white_line(im, pixel):
    
    if im[pixel.row][pixel.col] != Pixel.white:
        return 0
    
    im[pixel.row][pixel.col] = Pixel.black
    count = 1
    if pixel.row > 0 and im[pixel.row-1][pixel.col] == Pixel.white:
        count += count_white_line(im, Pixel(pixel.row, pixel.col, (0,0,0)))
    if pixel.row > len(im)-2 and im[pixel.row+1][pixel.col] == Pixel.white:
        count += count_white_line(im, Pixel(pixel.row+1, pixel.col, (0,0,0)))
    if pixel.col > 0 and im[pixel.row][pixel.col-1] == Pixel.white:
        count += count_white_line(im, Pixel(pixel.row, pixel.col-1, (0,0,0)))
    if pixel.col > len(im[0])-2 and im[pixel.row][pixel.col+1] == Pixel.white:
        count += count_white_line(im, Pixel(pixel.row, pixel.col-1, (0,0,0)))
    return count

def count_white_line2(im, pixel):
    
    try:
        if im[pixel.row][pixel.col] != Pixel.white:
            return 0
        im[pixel.row][pixel.col] = Pixel.black
    except:
        return 0
    
    count = 1
    count += count_white_line(im, Pixel(pixel.row, pixel.col, (0,0,0)))
    count += count_white_line(im, Pixel(pixel.row+1, pixel.col, (0,0,0)))
    count += count_white_line(im, Pixel(pixel.row, pixel.col-1, (0,0,0)))
    count += count_white_line(im, Pixel(pixel.row, pixel.col-1, (0,0,0)))
    return count

def count_white_line_iterative(im, pixel):
    if im[pixel.row][pixel.col] != Pixel.white:
        return 0
    count = 0
    to_count = set([pixel])
    while to_count:
        pixel = to_count.pop()
        im[pixel.row][pixel.col] = Pixel.black
        count += 1
        if pixel.row > 0 and im[pixel.row-1][pixel.col] == Pixel.white:
            to_count.add(Pixel(pixel.row-1, pixel.col))
        if pixel.row > len(im)-2 and im[pixel.row+1][pixel.col] == Pixel.white:
            to_count.add(Pixel(pixel.row+1, pixel.col))
        if pixel.col > 0 and im[pixel.row][pixel.col-1] == Pixel.white:
            to_count.add(Pixel(pixel.row, pixel.col-1))
        if pixel.col > len(im[0])-2 and im[pixel.row][pixel.col+1] == Pixel.white:
            to_count.add(Pixel(pixel.row, pixel.col-1))
    return count  

