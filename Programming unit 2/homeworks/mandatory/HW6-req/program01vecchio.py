# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:54:46 2021

@author: Siria
"""

import images

def Buildings(text):
    
    buildings = []
    for row in text.split('\n'):
        if row:
            int_row = [int(b) for b in row.split(',')[:-1] if b]
            buildings.append([(int_row[i], int_row[i+1],\
                                   int_row[i+2], int_row[i+3],\
                                   int_row[i+4]) for i in range(0, len(int_row)-1, 5)])
    return buildings

def VerticalDimentions(buildings, spacing):
    
    row_centers = []
    height = spacing
    for row in buildings:
        row_height = max(b[1] for b in row)
        row_centers.append(height + row_height*0.5)
        height += row_height + spacing
    
    return height, row_centers

def HorizontalDimentions(buildings, spacing):
    
    buildings_widths = []
    max_width = 0
    for row in buildings:
        buildings_width = sum(b[0] for b in row)
        row_width = buildings_width + (len(row) -1)*spacing
        if(row_width  > max_width):
            max_width = row_width
        buildings_widths.append(buildings_width)
    
    return max_width + 2*spacing, [(max_width - buildings_widths[i]) / (len(buildings[i])-1 if len(buildings[i]) > 1 else 2)  for i in range(len(buildings))]
        

def MapValues(file_dati, spacing):
    
    file = open(file_dati, 'rt', encoding = 'utf-8')
    text = file.read()
    
    buildings = Buildings(text)
    height, row_centers = VerticalDimentions(buildings, spacing)
    width, spacings = HorizontalDimentions(buildings, spacing);
    
    return width, height, [(spacings[i], row_centers[i]) for i in range(len(row_centers))], buildings

def DrawMap(width, height, offsets, buildings, spacing):
    
    img = [[(0, 0, 0)] * width for _ in range(height)]
    
    for i in range(len(buildings)):
        posX = spacing
        for b in buildings[i]:
            if len(buildings[i]) == 1:
                posX += offsets[i][0]
            DrawRect(img, posX, offsets[i][1] - b[1]/2, b[0], b[1], (b[2], b[3], b[4]))
            posX += b[0] + offsets[i][0]
            
    return img

def DrawRect(img, posX, posY, width, height, color):
    
    for x in range(int(posX), int(posX + width)):
        for y in range(int(posY), int(posY + height)):
            img[y][x] = color
    

def ex(file_dati, file_png, spacing):
    
    width, height, offsets, buildings = MapValues(file_dati, spacing)
    img = DrawMap(width, height, offsets, buildings, spacing)
    images.save(img, file_png)
    
    return (width, height)



