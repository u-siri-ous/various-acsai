#part 1 - function definition

def checkPassword(testString):  #<- function header "def"
    #here we check if the string has:
    #   at least 1 number
    #   no consecutive identical characters
    #   at least one #
    #return true if it does
    #return false if it doesn't
    #we assume that the string is 4 characters long
    #S="hello world", works like an array, and we have to check for indexes
    #if S[0] == "0":

    numbersCounter = 0

    #check which of the characters are numbers
    #backslash is used to split the condition in the editor but not in the program
    
    if testString[0] == "0" or testString[0] == "1" or \
    testString[0] == "2" or testString[0] == "3" or \
    testString[0] == "4" or testString[0] == "5" or \
    testString[0] == "6" or testString[0] == "7" or \
    testString[0] == "8" or testString[0] == "9":

    if testString[1] == "0" or testString[1] == "1" or \
    testString[1] == "2" or testString[1] == "3" or \
    testString[1] == "4" or testString[1] == "5" or \
    testString[1] == "6" or testString[1] == "7" or \
    testString[1] == "8" or testString[1] == "9":

    if testString[2] == "0" or testString[2] == "1" or \
    testString[2] == "2" or testString[2] == "3" or \
    testString[2] == "4" or testString[2] == "5" or \
    testString[2] == "6" or testString[2] == "7" or \
    testString[2] == "8" or testString[2] == "9":

    if testString[3] == "0" or testString[3] == "1" or \
    testString[3] == "2" or testString[3] == "3" or \
    testString[3] == "4" or testString[3] == "5" or \
    testString[3] == "6" or testString[3] == "7" or \
    testString[3] == "8" or testString[3] == "9":
        
        numbersCounter = numbersCounter+1

    if numbersCounter < 1:
        return False

    if testString[0] == testString[1] or \
    testString[1] == testString[2] or \
    testString[2] == testString[3]:
        return False

    if testString[0]!="#" and testString[1]!="#" \
    testString[2]!="#" and testString!="#":
        return False
    
    return True

#part 2 - calling the function with wanted string

myPassword = "b6w#"
print(checkPassword(myPassword))
        
