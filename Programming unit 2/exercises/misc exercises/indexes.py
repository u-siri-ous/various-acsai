# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:26:40 2021

@author: Siria
"""
L = ['hello', 8, True, 'ao', -9, '*', 1]
D = dict()

D['hello'] = 10
D['apple'] = 5
D[9] = True

def occurrencies(l):
    elements = [l.count(x) for x in range(len(l))]
    print(elements)
    elements2 = [index for (index,value) in enumerate(l) if value == 3]
    print(elements2)

def myFunc(myList):
    counter = 0
    for index, value in enumerate(myList):
        if value == 1:
            myList[index] = 0
            counter += 1
    return counter

L1 = [1,0,1,0,1,0]
checkL1 = L1.copy()

if myFunc(L1) == 3:
    print('it works')
else:
    print('no')
    
if checkL1 != L1:
    print('n o')   
    
if myFunc(L1) == 3:
    print('it works')
else:
    print('no')
      
if __name__ == "__main__":
    occurrencies([5,4,3,3,1,4,5,3,1,2])