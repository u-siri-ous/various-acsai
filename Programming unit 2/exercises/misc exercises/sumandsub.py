#Write a function that gets five integers
#as an input and returns the sum of all even numbers minus the sum of all odd numbers

def sum_sub(n1, n2, n3, n4, n5): #instead of n1, n2, n3, n4, n5, using lists 
    counter = 0
    if n1 % 2 == 0:
        counter = counter + n1
    else:
        counter = counter - n1
    if n2 % 2 == 0:
        counter = counter + n2
    else:
        counter = counter - n2    
    if n3 % 2 == 0:
        counter = counter + n3
    else:
        counter = counter - n3
    if n4 % 2 == 0:
        counter = counter + n4
    else:
        counter = counter - n4
    if n5 % 2 == 0:
        counter = counter + n5
    else:
        counter = counter - n5
    print(counter)
    return counter
