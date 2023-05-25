# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:38:55 2021

@author: Siria
"""
import pronouncing as p
import math


def RemovePunctuation(text):
    
    stripped = ''.join(ch if ch.isalpha() or ch == '\n' else ' ' for ch in text)
    
    return stripped


def ConvertToList(text):
    
    return [line.split() for line in text.split('\n') if line.split()]


def ConvertToStresses(word):
    
    phone = p.phones_for_word(word)
    if phone:
        return p.stresses(phone[0]).replace('2', '0')
    return '0' * (len(word)//2)


def StressesList(text_list):
    
    stresses = []
    for line in text_list:
        stresses.append(''.join(ConvertToStresses(word) + '0' for word in line))
    
    return stresses


def TextMatrix(string_list):
    
    max_length = max(len(l) for l in string_list)
    string = '\n'.join([l + '0' * (max_length-len(l)) for l in string_list])
    
    return string


def MakeTextMatrix(inputfilename):
    
    input_file = open(inputfilename, 'rt', encoding = 'utf-8')
    text = RemovePunctuation(input_file.read())
    input_file.close()
    
    stresses = StressesList(ConvertToList(text))
    
    return TextMatrix(stresses)   
        
    
def WriteFile(outputfilename, text_matrix):
    output_file = open(outputfilename, 'w')
    output_file.write(text_matrix)
    output_file.close()
    
    return


def CompressMatrix(text_matrix):
    
    splitted = text_matrix.split('\n')
    length = len(splitted[0])
    compressed = [[j for j in range(length) if line[j] == '1'] for line in splitted]
    
    return compressed

def CompareStress(x, list_, tau):
    
    min_pos = x-tau if tau<x else 0
    for y in list_:
        if y>x :    
            return 0
        if y>=min_pos :  
            return 1
    return 0
            
      
def CompareStressList(A, B, tau):
    
    return sum(CompareStress(x, B, tau) for x in A)    


def PairSync(A, B, tau):
    
    mA, mB = len(A), len(B)
    if not(mA and mB) :  return 0
    cAB = CompareStressList(A, B, tau)
    cBA = CompareStressList(B, A, tau)
    sync = 0.5 * (cBA + cAB) / math.sqrt(mA * mB)
    
    return sync


def Sync(matrix, tau):
    
    length = len(matrix)
    if length < 2: return 0
    sync = 0 
    for i in range(length):
        for j in range(i+1, length):
            sync += PairSync(matrix[i], matrix[j], tau)
    sync /= (length-1)*length/2 
    
    return sync


def PoemSync(inputfilename, outputfilename, tau):
    
    text_matrix = MakeTextMatrix(inputfilename)
    WriteFile(outputfilename, text_matrix)
    compressed_matrix = CompressMatrix(text_matrix)
    
    return round(Sync(compressed_matrix, tau), 6)