# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:53:37 2022

@author: Siria
"""

def processImage(matrix):
    
# =============================================================================
#     for num, x in enumerate(matrix):
#         print(num, x)
# 
# =============================================================================

# =============================================================================
#     for num in matrix:
#         x = matrix[0].index(num[0])
#         print(matrix.index(num), matrix[matrix.index(num)], x)
# =============================================================================
    if all(matrix):
        print("ao")
        if matrix[0] == [0,0,0]:
            return matrix
        
    
processImage([[0,0,0],[0,0,0]])