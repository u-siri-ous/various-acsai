# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:43:35 2021

@author: Siria

recap map and filter
"""

def mapfilter(filename):
    
    with open(filename) as f:
        text = f.read()
        string_list = text.split()
        #[int(w) for w in string_list] first way
        int_list = list(map(int, string_list))
    return int_list

def freq_file(filename):
    
    dic = {}
    line_cnt = 0
    with open(filename) as f:
        for line in f:
            line_cnt += 1
            line = line.strip()
            for char in line:
                #getting the key if it's present, it it's not create empty set
                dic[char] = dic.get(char, set()) | {line_cnt}
    return {k:list(v) for k,v in dic.items()}