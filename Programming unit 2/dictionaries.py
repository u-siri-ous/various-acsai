'''
dictionaries - associates values to words or other things
keys = words and other things
values = numeric values of elements
created by:
    dict_name{} or dictionary constructor dict()
syntax:
    name = {'word':value} or name['word'] = value
lists can be given as values
'''

testdict={'apple':2, 'pear':5, 'banana':3, 'peach':3}

#prints number of occurrencies

l = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3]
def count_numbers(alist):
    d = {}
    for number in alist:
        if number not in d:
            d[number] = alist.count(number)
    for k in d.keys():
        print(k, d[k])
        
def count_numbers2(alist):
    d = {}
    for number in alist:
        if number not in d:
            d[number] = 1
        else:
            d[number] += 1
    
