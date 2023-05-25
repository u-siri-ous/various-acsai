# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:25:03 2021

@author: Siria

Write a function that gets as an input two filenames and generates a dictionary.
Every file has a number of lines with some words separated by whitespaces.
Considering only the lines with exactly two words, you can build a dictionary
from both files. 
The function has to return a dictionary where the keys are the keys 
in both the dictionaries built from the files and the values are the
values joined by a '-' (minus sign), ordered in lexicographical order.
PSEUDOCODE
1)open 2 files
2)for each file read every line and build a dict only with the lines that have 2 words
3)compare the dicts to see the keys in common
4)for every key in common, generate a new key in a new dict with the two values combined

Write a function that gets a list of integers and sort it according to 
the reminder of the division for 11 and in case of a tie according to 
the reminder of the division for 5 and in case of further tie, in increasing order

Write a function that gets as input two filenames and it reads the content of
the first file and saves the same content in the second file, sorted line-by-line
according to the initial letter. In case of tie, by the lenght of the line.
In case of tie, by the position of the line in the first file.
"""
# =============================================================================
# with open(file1) as f:
# with open(file2) as f:
# =============================================================================
def build_dict(file):
    new_dict = {}
    with open(file) as f:
        for line in f:
            words = line.split()
            if len(words) == 2:
                new_dict[words[0]] = words[1]
    return new_dict
        
def build_from_files(file1,file2):
    dict1 = build_dict(file2)
    dict2 = build_dict(file2)
    new_dict = {}
    for key in dict1:
        if key in dict2:
            val1 = dict1[key]
            val2 = dict2[key]
            if val1 < val2:
                new_dict[key] = val1 + '-' + val2
            else:
                new_dict[key] = val2 + '-' + val1
            #new_dict[key] = min(val1, val2) + '-' + max(val1, val2)
    return new_dict

def sort_reminder(l):
    return sorted(l, key = lambda x : (x%11, x%5, x))

def sort_file(file1, file2): 
    with open(file1) as f:
        lines = f.readlines()
    lines = sorted(lines, key = lambda string : (string[0], len(string), lines.index(string)))
    with open(file2, 'w') as f:
        f.writelines(lines)
    


    
    
    