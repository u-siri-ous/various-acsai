# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:32:06 2021

1)Write a function that gets a list of floats as input and returns a dictionary
with 2 keys, where the values are the lists of the positive and negative numbers
[3.4, -2.5, 1.2, -0.5] -> {'positive' : [3.4, 1.2], 'negative' : [-0.5, -2.5]}

2)Write a function that gets as input two lists with equal number of elements and
returns a dictionary where the keys are the values of the first list and the 
values are the elements of the second list

3)Write a function that gets as input a string and returns a list containing all the
words of the input string, ordered by the number of vowels in the word
in case of a draw use the words length, in case of a further draw, use the 
alphabetic order
['apple,pineapple,coconut,pear,peach,mango,chestnut'] -> count vowels and order the words

4)Write a function that reads the content of a file taken as an input and returns
a dictionary with the frequencies of the letters in the file
file.txt contains "aaabb" -> {'a':3, 'b':2}

5)Write a function that gets a list ena d afile name and writes in a new file with name
filename the unique elements in list with the number of times every element is repeated
in the list. in the file the element and the number of its reps is separated by a tab
"""
#ex 1
def float_dict(float_list):
    #one liner solution
    d = {"positive":[x for x in float_list if x >= 0],
         "negative":[x for x in float_list if x < 0]}
    return d
# =============================================================================
# extended of the one liner
#     def float_dict(float_list):
#     d = {'positive':[], 'negative':[]}
#     for x in float_list:
#         if x >= 0:
#             d['positive'].append(x)
#         else:
#             d['negative'].append(x)
#     return d
# =============================================================================

#ex 2
def build_dict(key_list, value_list):
    d = {}
    for i in key_list:
        d[key_list[i]] = value_list[i]
    return d
#return {i:j for i,j in zip(key_list, value_list)} faster soluion

#ex 3
def vowels_list(string):
    def count_vowels(s):
        counter = 0
        for c in s:
            if c in 'aeiou':
                counter += 1
        return counter
    words = string.split(',')
    #return sorted(words)
    words.sort(key = lambda word : (count_vowels(word), len(word), word))
    print(words)
    return words

#ex 4 (class)
def file_freq(myfile):
    d = {}
    with open(myfile) as f: #f = open(myfile)
        for char in f.read():
            d[char] = d.get(char, 0) + 1
            #if char not in d:
                #d[char] = 1
            #else:
                #d[char] += 1
    return d

#ex 5 (class)
def write_list_reps(mylist, filename):
    dic = {}
    for element in mylist:
        if element not in dic:
            dic[element] = mylist.count(element)
    with open(filename, 'w') as fh:
        for k, v in dic.items():
            print(k, '\t', v, file = fh)

if __name__ == "__main__":
    #ex 1
    float_dict([3.4, -2.5, 1.2, -0.5])
    #ex 2
    build_dict([0,1,2,3],[4,5,6,7])
    #ex 3
    vowels_list('apple,pineapple,coconut,pear,peach,mango,chestnut')