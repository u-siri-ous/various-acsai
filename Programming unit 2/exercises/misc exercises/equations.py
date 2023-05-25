#programs that solves 2nd grade equation and displays the highest result

def equation(a, b, c):
    result1=(-b-(b**2-4*a*c)**0.5)/(2*a)
    result2=(-b+(b**2-4*a*c)**0.5)/(2*a)
    print(result1, result2)
    return max(result1, result2) #returns the biggest number without all the hassle below
#    if result1 < result2:
#        print('The highest result is: ', result2)
#        return result2
#    else if result1 > result2:
#        print('The highest result is: ', result1)
#        return result1

    
