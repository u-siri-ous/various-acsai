# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:34:50 2021

@author: Siria

exceptions are the handling of errors
basically you can program response to errors in your program

"""
from rtrace import trace
#L = ['hello', 4, 'ciao', 2, 'bonjour', 6]
# =============================================================================
# print(L[3]) error! index out of range (IndexError), this makes the program stop, so no
#             further expressions will be executed
# try:
#     print(L[3])
# except:
#     raise IndexError('check your indexes!') #this programs a specific error, therefore raises expected errors
#     #or pass, this gives no explanation, just IndexError
#     
# acc = 0
# acc_ = ''
# for item in L:
#     try:
#         acc += item
#     except:
#         acc_ += item
# 
# =============================================================================
@trace 
def PalindromeRecursive(s, start, end):
# =============================================================================
#     check if 1st == last:
#       different -> False
#       equal -> discard 1st, last
#             -> recur on the remaining characters
# =============================================================================
    if (start-end)<=1:
        return True
    if s[start] != s[end]:
        return False
    else:
        s.pop(0)
        s.pop(len(s)-1)
        return PalindromeRecursive(s, start+1, end-1)
    
if __name__ == '__main__':
    word = list('rotator')
    print(PalindromeRecursive.trace(word, 0, len(word)-1))
    