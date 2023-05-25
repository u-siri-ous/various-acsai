# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:53:36 2021

@author: Siria
"""

'''
Write a function that takes as an input a list of strings and finds the letter which
appears more times as the final letter of all the strings in the list
['apple', 'pear', 'banana', 'peach', 'pineapple'] -> returns 'e'
'''

def last_letter(stringlist):
    d = {}
    for word in stringlist:
        if word[-1] in d:
            d[word[-1]] += 1
        else:
            d[word[-1]] = 1
    firstword = stringlist[0]
    maxkey =  firstword[-1]
    maxval = d[maxkey]
    for key in d:
        if d[key] > maxval:
            maxkey = key
            maxval = d[key]
    return maxkey
    
    def criteria(key):
        return d[key]
    return max(d, key = criteria)