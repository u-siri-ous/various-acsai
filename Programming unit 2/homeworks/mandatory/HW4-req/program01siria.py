# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:38:55 2021

@author: Siria
"""
import pronouncing as p
import math


def RemovePunctuation(text):
    
    punctuations = "!\"#$%&()*+,./:;<=>?@[\]^_`{|}~"
    table = str.maketrans('\'-—', '   ', punctuations)
    
    return text.translate(table)


def ConvertToList(text):
    
    return [line.split() for line in text.split('\n') if line.split()]


def ConvertToStresses(word):
    
    phone = p.phones_for_word(word)
    if phone:
        return p.stresses(phone[0]).replace('2', '0')
    return '0' * (len(word)//2)

def StressesList(text_list):
    
    stresses_list = []
    for line in text_list:
        s_string = ''.join(ConvertToStresses(word) + '0' for word in line)
        stresses_list.append(list(map(int, s_string)))
    
    return stresses_list


def ConvertToMatrix(nested_list):
    
    max_length = max(len(l) for l in nested_list)
    
    return [l + [0] * (max_length-len(l)) for l in nested_list]

def MakeMatrix(inputfilename):
    
    input_file = open(inputfilename, 'rt', encoding = 'utf-8')
    text = RemovePunctuation(input_file.read())
    input_file.close()
    
    stresses = StressesList(ConvertToList(text))
    
    return ConvertToMatrix(stresses)   

def MatrixToString(matrix):
    text = str()
    for row in matrix:
        line = ''.join(str(i) for i in row) + '\n'
        text += line
    
    return text
        
    
def WriteFile(outputfilename, matrix):
    output_file = open(outputfilename, 'w')
    output_file.write(MatrixToString(matrix))
    
    return


def CompareStress(x, A, tau):
    
    for y in range(x-tau if x >= tau else 0, x+1):
        if A[y]:    
            return 1
    return 0
                  
def CompareStressList(A, B, tau):
    
    return sum(CompareStress(x, B, tau) for x in range(len(A)) if A[x])

def PairSync(A, B, tau):
    
    mA = sum(A)
    mB = sum(B)
    
    if(not mA or not mB):  
        return 0
        
    cAB = CompareStressList(A, B, tau)
    cBA = CompareStressList(B, A, tau)
    sync = 0.5 * (cBA + cAB) / math.sqrt(mA * mB)
    
    return sync

def Sync(matrix, tau):
    
    length = len(matrix)
    sync = 0
    for i in range(length):
        for j in range(i+1, length):
            sync += PairSync(matrix[i], matrix[j], tau)
    sync /= (length-1)*length/2     #Formula somma n numeri naturali
    
    return sync


def PoemSync(inputfilename, outputfilename, tau):
    
    matrix = MakeMatrix(inputfilename)
    WriteFile(outputfilename, matrix)
    
    return round(Sync(matrix, tau), 6)

if __name__ == "__main__":
    # your tests go here
    pass