#write a function that gets a string as an input and returns another string
#with only the vowels found in the original string in the same order

def stringvowels(string):
    new_string = ''
    for char in string:
        if char in 'aeiou':
            new_string += char
    return new_string

#write a function that returns the number of values in a string

def countvowels_1(string):
    new_string = ''
    for char in string:
        if char in 'aeiou':
            new_string += char
    return len(new_string)

def countvowels_2(string):
    count = 0
    new_string = ''
    for char in string:
        if char in 'aeiou':
           count += 1
    return count
