# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:33:21 2021

@author: Siria
"""

'''
Write a function that takes as an input a list of integers
and prints on the screen all the numbers in the list once
with the times a certain element appears in the list
list elements must be between 0 and 1000
'''
import random
from math import inf

def count_int(mylist):
    timeselement = 0
    mylist.sort()
    for element in range(len(mylist) - 1):
        if mylist[element] == mylist[element + 1]:
            timeselement += 1
    print(mylist, timeselement + 1)
    
alist = [random.randint(0,1000) for _ in range(10000)]
count_int(alist)