# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:22:20 2021

@author: Siria

given a list of elements, write a recursive function that generates all the possible permutation of the list
(permutations of all the elements in different order)

"""

def fact(x): #1 if x == 0, else x * fact(x-1)
    if x == 0:
        return 1
    elif x < 0:
        raise ValueError('the number must be positive')
    else:
        return x * fact(x-1)
            
def fib(x):
    if 0 <= x <= 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
def pali(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and pali(word[1:-1])
    
def permutations(alist):
    #fix the first element
    #compute all the possible values
    #fix another starting element
    #repeat
    f_perm = []
    if len(alist) == 1:
        return [alist]
    for i,el in enumerate(alist):
        all_perm = permutations(alist[:i]+alist[i+1:])
        for p in all_perm:
            f_perm.append([el]+p)
    return f_perm

def sum_up(alist):
    if len(alist) == 1:
        return alist[0]
    return alist[0] + sum_up(alist[1:])

def suffixes(string):
    #ex: hello o,lo,llo,ello,hello
    if len(string) == 1:
        return [string]
    return [string] + suffixes(string[1:])

def suffix(string, i=0):
    if len(string) == i+1:
        return [string[i:]]
    return [string[i:]] + suffix(string, i+1)

def prefixes(string):
    if len(string) == 1:
        return [string]
    return [string] + prefixes(string[:-1])

def prefix(string, i=0):
    if len(string) == i+1:
        return [string]
    return [string[:-i]] + prefix(string, i+1)
    
