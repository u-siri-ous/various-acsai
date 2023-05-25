# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:38:55 2021

@author: Siria
"""
import pronouncing as p
# =============================================================================
# 
# def phonetics(filename):
#     stresslist = list()
#     with open(filename, 'r+') as f:
#         for line in f:
#             l_stresses = list()
#             for word in line.split():
#                 phones = p.phones_for_word(word)
#                 if phones:
#                     stresses = list(p.stresses(phones[0]))
#                     if '2' in stresses:
#                         stresses[stresses.index('2')]= '0'
#                     l_stresses += stresses
#                 else:
#                     for x in range(len(word)//2):
#                         l_stresses.append('0')
#                 l_stresses.append('0')
#             stresslist.append(l_stresses)
#             
#         fixMatrix(stresslist)
#         return stresslist
#     
# def fixMatrix(matrix):
#     max_length = max(matrix, key = lambda line: len(line))
#     max_length = len(max_length)
#     for line in matrix:
#         for x in range(len(line), max_length):
#             line.append('0')
# 
# =============================================================================

    
def phonetics(filename):
    stress_matrix = list();
    stress_line = list();
    a = str()
    punctuation = {44 : None}
    with open(filename, 'r+') as f:
        for l in f:
            a = str(l)
            a = a.translate(punctuation)
            print(a)
            stress_line = []
            for w in l.split():
                phones = p.phones_for_word(w)
                if phones:
                    stresses = p.stresses(phones[0])
                    for s in stresses:
                        if s == '1':
                            stress_line.append('1')
                        else:
                            stress_line.append('0')
                else:
                    stress_line+= ['0']*(len(w)//2)
                stress_line.append('0')
            stress_matrix.append(stress_line)
    
    return stress_matrix
    
    
                
                
                
                
                