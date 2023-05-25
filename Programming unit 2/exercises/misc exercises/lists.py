#write a function that takes a list of int as an input and outputs a new list
#with only the elements of the original list that are divisors of 210

def listdivisor(values):
    newlist = []
    for element in values:
        if 210 % element == 0:
#            divisor = list(element) lists are not iterable!!! do like this:
            newlist.append(element)
        else:
            pass
    return newlist

#generalising it to every number:

def divisors(number, values):
    newlist = []
    for element in values:
        if number % element == 0:
            newlist.append(element)
        else:
            pass
    return newlist
