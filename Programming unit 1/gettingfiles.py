# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:23:13 2021

@author: Siria
"""

import os

allfiles = {}

def GetFiles(folderName, d):
    files = os.listdir(folderName)
    print(files)
    for f in files:
        f = folderName + '\\' + f
        if os.path.isdir(f):
            GetFiles(f, d)
            #print(f, '(folder)')
        else:
            d[f] = f
            #print(f, '(file)')
            
if __name__ == '__main__':
    GetFiles(r'C:\Users\Lenovo\Desktop\Analisi & Moduli', allfiles) #raw string works idk 
    print(list(allfiles.keys))