#Write a function that asks the user for three grades as input (using the input function)
#and returns the average of the grades only if all the grades are legitimate
#(i.e. 0<=grade<=30), returns False otherwise

def ave():
    g1 = int(input('First grade: '))
    g2 = int(input('Second grade: '))
    g3 = int(input('Third grade: '))
    if 0<=g1<=30 and 0<=g2<=30 and 0<=g3<=30:
        return (g1+g2+g3)/3
    else:
        return False
