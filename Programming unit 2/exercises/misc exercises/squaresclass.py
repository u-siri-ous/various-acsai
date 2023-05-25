# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:45:29 2021

@author: Siria
"""

from classes import Point

class Square:
    def __init__(self, p, side):
        if type(p) != Point:
            raise TypeError('not a point')
        self.p = p
        self.side = side
        
    def __repr__(self):
        #p =  self.p.__repr__
        return f"Square({self.p}, Side{self.side})"
    
    def __str__(self):
        return self.__repr__
    
    def perimeter(self):
        return self.side * 4
    
    def area(self):
        return self.side ** 2
    
class Rect:
    def __init__(self, p1, p2):
        if type(p1) != Point or type(p2) != Point:
            raise TypeError ('not points')
        self.p1 = Point(min(p1.x, p2.x), max(p1.y, p2.y))
        self.p3 = Point(max(p1.x, p2.x), min(p1.y, p2.y))
        self.p2 = Point(p2.x, p1.y)
        self.p4 = Point(p1.x, p2.y)
        
    def perimeter(self):
        return (self.p1.distanceFromP(self.p2) + self.p1.distanceFromP(self.p3)) * 2