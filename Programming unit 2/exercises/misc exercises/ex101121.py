# -*- coding: utf-8 -*-
"""
1) Write a function that can be used as a key function for sorting a list of integers 
   so that: all the odd integers appear sorted in increasing order before the even ones,
   sorted in decreasing order
2) Write a function that gets a filename as input and returns a list. The filename 
   is the name of a file containing several words on several lines, separated by 
   spaces. The list includes an integer for each word in the file, summing up 
   the Unicode values of the characters that compose the string (use 'ord' function).
3) Write a function that gets a list as an input and removes from the list all the 
   elements that are identical and close to eachother in the list
"""
#1
def mykey(i):
    return -(i % 2 -1)/i
#2
def ord_word(word):
    s = 0
    for c in word:
        s += ord(c)
        return s
    
def tolist(file):
    l = []
    with open(file) as f:
        for lines in f:
            for word in l:
                #l.append(ord_word(word))
                l.append(sum(map(ord,word)))
    return l

#3
def remove_identical(lst, i = 0):
    if i == len(lst) - 1:
        return 
    if lst[i] == lst[i+1]:
        lst.pop(i)
    else:
        i += 1
    remove_identical(lst, i)
# =============================================================================
#     deleted = 0
#     for i in range(len(lst)-1, 0, -1):
#         if lst[i] == lst[i - deleted + 1]:
#             del lst[i - deleted + 1]
#             deleted += 1
# =============================================================================

def relative_frequency(dictionary, file):
    d = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
    with open(file) as f:
        text =  f.read()
    text = text.lower()
    total = sum(d.values())
    
        


            
    

    
            
 