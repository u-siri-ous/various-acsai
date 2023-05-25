# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:29:56 2021

@author: Siria
"""

import pngmatrix

def AveragePixels(pixels):
    pixel = [0,0,0]
    for p in pixels:
        pixel[0] += p[0]
        pixel[1] += p[1]
        pixel[2] += p[2]
    pixel[0] //= len(pixels)
    pixel[1] //= len(pixels)
    pixel[2] //= len(pixels)
    return tuple(pixels)
        
def GetSquare(img,x,y,thickness):    
    x_s = max(0, x - thickness)
    x_e = min(x + thickness + 1, len(img[y]))
    y_s = max(0, y - thickness)
    y_e = min(y + thickness + 1, len(img))
    pixels = list()
    
    for x_i in range(x_s, x_e):
        for y_i in range(y_s, y_e):
            pixels.append(img[y_i][x_i])
    return pixels

def Blur(img,amount):
    result_i = list()
    for x_i in range(len(img[0])):
        result_row = []
        for y_i in range(len(img)):
            result_row.append(AveragePixels(GetSquare(img, x_i, y_i, amount)))
        result_i.append(result_row)
    return result_i

if __name__ == "__main__":
    image = pngmatrix.load_png8("Plato.png")
    print(GetSquare(image, 0, 0, 1))

