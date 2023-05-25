# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:34:27 2021

@author: Siria
"""
#import copy to use deep copy

class Matrix:
    def __init__(self, list_lists):
        if type(list_lists) != list or any(map(lambda x : type(x)!=list, list_lists)):
            raise TypeError
        for l in list_lists:
            if any(map(lambda x : not isinstance(x, (int, float)), l)) or len(l) != len(list_lists[0]):
                raise TypeError
        self.mat = [list_.copy() for list_ in list_lists]
        self.rows = len(list_lists)
        self.cols = len(list_lists[0])
        
    def __repr__(self):
        return f'Matrix({self.rows}x{self.cols})'
    
    def __str__(self):
        pass
    
    def __add__(self, m):
        new_m = []
        if self.rows != m.rows or self.cols != m.cols:
            raise TypeError
        for a, b in zip(self.mat, m.mat):
            new_m.append([a[x]+b[x] for x in range(len(a))])
        return Matrix(new_m)
            
                
                   