# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:25:26 2021

@author: Siria
"""
'''
Write a function that takes as an input a string
and returns a disct with the character frequency,
namely for evety character it counts the number 
of repetitions and creates a key with the number
of repetition as the value
'''
def repetitions(astring):
    d = {}
    astring2 = list(astring)
    for c in astring2:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
# =============================================================================
#     for k in d.keys():
#         print(k, d[k])
# =============================================================================
    print(d, d.items())


if __name__ == "__main__":
    repetitions('hello')
