# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:20:10 2021

@author: Siria
"""

def text(file):
    with open(file, "r", encoding = "utf-8") as f:
        a = f.read()
        a = a.replace(",", "").replace("\t", "")
        print(a.split())