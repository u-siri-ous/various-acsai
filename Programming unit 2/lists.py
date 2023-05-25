#write a function that returns the sum of elements of a list taken as an input
def list_sum(values):
    partialres=0
    for element in values:
        partialres = partialres + element
    return partialres

#write a function that returns the sum of the even elements of a list taken as an input
def evensum(values):
    res_even=0
    for element in values:
        if element % 2 == 0:
            res_even += element
        else:
            pass
    return res_even
            
#write a function that returns the sum of the even elements of a list taken as an input minus
#the sum of the odd numbers
def sumsub(values):
    res_even=0
    res_odd=0
    for element in values:
        if element % 2 == 0:
            res_even += element
        else:
            res_odd += element
    return res_even - res_odd    
#solution with one variable for partial result
def sumsub_onevar(values):
    res=0
    for element in values:
        if element % 2 == 0:
            res += element
        else:
            res -= element
    return res
