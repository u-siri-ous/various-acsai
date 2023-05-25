# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:54:46 2021

@author: Siria
"""

import images

def TupleElements(int_row):
    '''
    

    Parameters
    ----------
    int_row : List
        Implementation of quintuple divided text

    Returns
    -------
    Structure to divide the text

    '''
    
    return [(int_row[i], int_row[i+1], int_row[i+2], int_row[i+3], int_row[i+4]) for i in range(0, len(int_row)-1, 5)]

def Buildings(text):
    '''
    

    Parameters
    ----------
    text : Text file
        DESCRIPTION.

    Returns
    -------
    buildings : TYPE
        DESCRIPTION.

    '''
    
    buildings = []
    for row in text.split('\n'):
        if row:
            int_row = [int(b) for b in row.split(',')[:-1] if b]
            buildings.append(TupleElements(int_row))
    return buildings

def MinWidth(buildings, spacing):
    """
    

    Parameters
    ----------
    buildings : TYPE
        DESCRIPTION.
    spacing : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    '''
    '''
    
    return max(sum(b[0] for b in row) + spacing * (len(row)-1) for row in buildings)

def MakeMapRow(row, spacing, startY, min_width):
    '''
    

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.
    spacing : TYPE
        DESCRIPTION.
    startY : TYPE
        DESCRIPTION.
    min_width : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    posX, posY = spacing, startY
    length = len(row)
    if length == 1:
        return [(posX + (min_width - row[0][0])/2, posY - row[0][1]/2, row[0])]
    dist = (min_width - sum(b[0] for b in row))//(length-1)
    map_row = []
    for b in row:
        map_row.append((posX, posY - b[1]//2, b))
        posX += b[0] + dist
    
    return map_row

def ReadFile(file_dati):
    '''
    

    Parameters
    ----------
    file_dati : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    file = open(file_dati, 'rt', encoding = 'utf-8')
    text = file.read()
    
    return Buildings(text)

def MakeMapMatrix(file_dati, spacing):
    '''
    

    Parameters
    ----------
    file_dati : TYPE
        DESCRIPTION.
    spacing : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    buildings = ReadFile(file_dati)
    min_width = MinWidth(buildings, spacing)
    borders = spacing * 2
    
    map_matrix = []
    posY = spacing
    for row in buildings:
        half_max_height = max(b[1] for b in row)//2
        posY += half_max_height
        map_matrix.append(MakeMapRow(row, spacing, posY, min_width))
        posY += half_max_height + spacing
        
    return map_matrix, (min_width + borders, posY)


def MakeMapImage(map_matrix, img_dim):
    '''
    

    Parameters
    ----------
    map_matrix : TYPE
        DESCRIPTION.
    img_dim : TYPE
        DESCRIPTION.

    Returns
    -------
    img : TYPE
        DESCRIPTION.

    '''
    
    img = [[(0, 0, 0)] * img_dim[0] for _ in range(img_dim[1])]
    
    for row in map_matrix:
        for b in row:
            DrawRect(img, b[0], b[1], b[2][0], b[2][1], tuple(b[2][2:5]))
    
    return img
    

def DrawRect(img, posX, posY, width, height, color):
    '''
    

    Parameters
    ----------
    img : TYPE
        DESCRIPTION.
    posX : TYPE
        DESCRIPTION.
    posY : TYPE
        DESCRIPTION.
    width : TYPE
        DESCRIPTION.
    height : TYPE
        DESCRIPTION.
    color : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    for x in range(int(posX), int(posX + width)):
        for y in range(int(posY), int(posY + height)):
            img[y][x] = color
    

def ex(file_dati, file_png, spacing):
    '''
    

    Parameters
    ----------
    file_dati : TYPE
        DESCRIPTION.
    file_png : TYPE
        DESCRIPTION.
    spacing : TYPE
        DESCRIPTION.

    Returns
    -------
    img_dim : TYPE
        DESCRIPTION.

    '''
    
    map_matrix, img_dim = MakeMapMatrix(file_dati, spacing)
    img = MakeMapImage(map_matrix, img_dim)
    images.save(img, file_png)
    
    return img_dim




