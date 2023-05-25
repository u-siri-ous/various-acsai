#Write a function that takes as an input a string with a sequence of words separated with
#whitespaces and returns a new list with the corresponding string length
#string = 'cabbage goat farm whatever'
#returns [7, 4, 4, 8]

#this just counts characters in a string and returns them as a list
def lengths(string):
    s=list(string)
    count=0
    characters=0
    whitespaces=0
    for element in string:
        if element[count] != chr(32):
            characters+=1
        elif element[count] == chr(32):
            whitespaces+=1
    return list[characters, whitespaces]

#now counting every word and returning them in a new list
def wordlength(string):
    s=string.split()
    characters=0
    whitespaces=0
    l=[]
    for element in s: #in this case "element" selects the list element to count,unlike a counter
        l.append(len(element))
    return l

def wordlength2(string):
    count=0
    characters=0
    whitespaces=0
    l=[]
    for char in string:
        if char != ' ':
            count+=1
        elif count!=0:
            l.append(count)
            count=0
        else:
            count=0
    if count!=0:
        l.append(count)
    return l 

def wordlength3(string):
    s=string.split()
    for i in range(len(s)):
        s[i]=len(s[i])
    return s 

