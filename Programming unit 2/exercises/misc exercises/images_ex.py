# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:07:00 2021

@author: Siria

Write a function that gets as input an image a row, col (coordinate(x,y)), pixel, 
a side_length and color and draws a square of color color with top left corner in 
pixel row, col and with side as side_length without filling it
it returns the number of pixels colored

"""
import images

im = [[(0,0,0)] * 400 for _ in range(300)]
images.save(im, 'test.png')

def draw_square(im, row, col, side_length, color):
    count = 0
    if row > len(im) or col > len(im[0]):
        return 0
    for i in range(col, min(col+side_length+1, len(im[0]))):
        im[row][i] = color
        count += 1
        if row+side_length < len(im):
            im[row+side_length][i] = color
            count += 1
    for i in range(row+1, min(row+side_length-1, len(im))):
        im[i][col] = color
        count += 1
        if col+side_length < len(im[0]):
            im[i][col+side_length] = color
            count += 1
    return count

def draw_rect(im, row, col, width, height, color):
    count = 0
    if row > len(im) or col > len(im[0]):
        return 0
    for i in range(col, min(col+width+1, len(im[0]))):
        im[row][i] = color
        count += 1
        if row+height < len(im):
            im[row+height][i] = color
            count += 1
    for i in range(row+1, min(row+height-1, len(im))):
        im[i][col] = color
        count += 1
        if col+width < len(im[0]):
            im[i][col+width] = color
            count += 1
    return count

if __name__ == '__main__':
    pass