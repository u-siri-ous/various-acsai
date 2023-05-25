#Write a function that takes as an input a list of integers and returns True if the list
#is ordered in an increasing order

#ordered([1,2,3,4])->True ordered([5,1,9,2])->False

def ordered(intlist):
    return intlist == sorted(intlist) #returns true if list is sorted, false otherwise

#this function compares the first element with the others, based on the fact that n should be
#bigger than n-1, so it controls every element of the list from list[0] to list[lastelement-1]
#if the previous contition isn't satisfied, we can say that the list is not increasing
def ordered2(intlist):
    for i in range(len(intlist)-1): #-1 is necessary to avoid out of range error
        if intlist[i] > intlist[i+1]: 
            return False
    return True
