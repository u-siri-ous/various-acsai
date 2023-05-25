# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:15:23 2021

@author: Siria

"""

class Point:
    
    def __init__(self, x=0, y=0):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
            
    def __repr__(self): #different from printing, defined in __str__
        return f"Point({self.x},{self.y})"
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distanceFromZero(self):
        return (self.x**2 + self.y**2)**0.5
        
    def distanceFromP(self, p):
        if type(p) != Point:
            raise TypeError
        X = (self.x - p.x)**2
        Y = (self.y - p.y)**2
        return (X+Y)**2