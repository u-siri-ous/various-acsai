# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:31:22 2021

@author: Siria

defining simple classes
"""
class Car:
    color = ''
    wheels_n = 4
    modelname = ''
    
    #constructor
    def __init__(self, c, m):
        self.color = c
        self.modelname = m
        
    #destructor
    def __del__(self):
        pass
        
    
    def Print(self):
        print(self.modelname, self.wheels_n, self.color)
    
if __name__ == '__main__':
# =============================================================================
#     car1 = Car()
#     car2 = Car()
#     car1.color = 'red'
#     car2.color = 'black'
#     car1.modelname = 'panda'
#     car2.modelname = 'ferrari'
# =============================================================================
    #using init
    car1 = Car('red','ferrari')
    car2 = Car('black', 'panda')
    car1.Print()
    car2.Print()