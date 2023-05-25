# -*- coding: utf-8 -*-

'''
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
    – takes as parameters 
      a string (int_seq) and a positive integer (subtotal >= 0), and 
    – returns the number of substrings of int_seq such that 
      the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
    elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,0,5,0,4,2' and subtotal = 9, 
    the function should return 7. The following substrings, indeed, consist of
    values whose sum is equal to 9:
    int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
            => _'0,4,0,3,1,0,1,0'_____________
               _'0,4,0,3,1,0,1'_______________
               ___'4,0,3,1,0,1,0'_____________
               ___'4,0,3,1,0,1'_______________
               ___________________'0,0,5,0,4'_
               _____________________'0,5,0,4'_
               _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
    1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)
'''
# =============================================================================
# 
# def ex1s(int_seq,subtotal):
#     newlist = [int(x) for x in int_seq.split(",")]
#     #newlist = int_seq.split(",")
#     stringtotal = 0
#     total = 0
#         
#     #for i in range(len(newlist)): 
#     #    newlist[i]= int(newlist[i])
#     
#         
#     for i in range(len(newlist)): #index of starting element
#         for j in range(i,len(newlist),1): #sum elements for(int j=i; j<newlist.length();j++)
#             
#             total += newlist[j] #doing the sum between elements
#                 
#             if(total==subtotal):
#                 stringtotal+=1
#             elif(total > subtotal):
#                 break
#             
#         total = 0
#         
#     return stringtotal
# =============================================================================

def ex1(int_seq, subtotal):
    stringtotal = 0
    
    for i in range(0, len(int_seq)-1, 2):
        total = 0
        for j in range(i, len(int_seq)-1, 2):
            total += int(int_seq[j])
                
            if(total==subtotal):
                stringtotal+=1
            elif(total > subtotal):
                break
            
    return stringtotal
            
            
             
if __name__ == "__main__":
    print(ex1("1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 3))
    