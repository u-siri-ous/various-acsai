#Write a function that gets three integers as an input d, m, y
#(it is assumed that a is always an odd number to avoid leap years)and returns True or False
#depending on whether the three numbers form a valid date in the "d/m/y" format.
#Ex: 30/2/2017 False (doesn't exist), 1/1/1111 True

#introducing elif / else if and tuples

def dates(d, m, y):
    #d = int(input('Enter day: '))
    #m = int(input('Enter month: '))
    #y = int(input('Enter year: '))
    if y % 2 != 0:
        return True
    else:
        return False
    #if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    if m in (1,3,5,7,8,10,12):
        if 1 <= d <= 31:
            return True
        else:
            return False
    #elif m == 4 or m == 6 or m == 9 or m == 11:
    elif m in (4,6,9,11):
        if 1 <= d <= 30:
            return True
        else:
            return False
    elif  m == 2:
        if 1 <= d <= 28:
            return True
        else:
            return False
    else:
        return False
