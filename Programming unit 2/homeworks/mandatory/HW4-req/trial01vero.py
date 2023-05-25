# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:38:55 2021

@author: Siria
"""
import pronouncing as p
import math

def WorkOnFile(inputfilename):
    
    file = open(inputfilename, 'rt')
    text = RemovePunctuation(file.read())
    file.close()
    
    t_list = ConvertToList(text)
    phones = ConvertToPhones(t_list)
    stresses = ConvertToStresses(t_list, phones)
    matrix = ConvertToMatrix(stresses)
    
    with open("output.txt", 'w') as f:
        f.write(matrix)
    
    lenm = len(matrix)
    ma = 0 
    mb = 0

    for i in range(lenm - 1):
        ma = matrix[i].count(1)
        for j in range(i+1 ,lenm):
            mb = matrix[j].count(1)
        
    return ma, mb, matrix

def RemovePunctuation(text):
    
    punctuations = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    table = str.maketrans('\'', ' ', punctuations)
    
    return text.translate(table)   

def ConvertToList(text):
    
    t = [line.split() for line in text.split('\n') if line.split()]
    
    return t

def ConvertToPhones(text_list):
    
    phones_matrix = []
    for line in text_list:
        phones_matrix.append([p.phones_for_word(word) for word in line])
    
    return phones_matrix
                
def ConvertToStresses(text_list, phones):
    
    stresses_matrix = []
    for x in range(len(text_list)):
        stresses_row = []
        for y in range(len(text_list[x])):
            if phones[x][y]:
                stresses_row.extend(list(p.stresses(phones[x][y][0]).replace('2', '0')))
            else:
                stresses_row += ['0'] * (len(text_list[x][y])//2)
            stresses_row.append('0')
        stresses_matrix.append(stresses_row)
    
    return stresses_matrix

def ConvertToMatrix(nested_list):
    max_length = max(len(l) for l in nested_list)
    
    matrix = list(map(lambda l: l + ['0'] * (max_length-len(l)), nested_list))
    
    return matrix

def PoemSync(inputfilename, outputfilename, tau):
    
    WorkOnFile(inputfilename)
    
# =============================================================================
#     file = open(inputfilename, 'rt')
#     text = RemovePunctuation(file.read())
#     file.close()
#     
#     t_list = ConvertToList(text)
#     phones = ConvertToPhones(t_list)
#     stresses = ConvertToStresses(t_list, phones)
#     matrix = ConvertToMatrix(stresses)
# =============================================================================
    #sync = (0.5 * cba + cab)/math.sqrt(ma*mb)
    #return matrix

if __name__ == "__main__":
    # your tests go here
    pass