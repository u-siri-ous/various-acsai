# -*- coding: utf-8 -*-
"""
Write a function that gets a list of lists and returns true if the list 
can be considered a matrix, false otherwise

not isinstance() -> type(element) is not int and type(element) is not float:
"""
def matrix(m):
    length = len(m[0])
    for row in m:
        if len(row) != length:
            return False
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True
                

