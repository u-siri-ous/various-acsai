# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:16:21 2021

@author: Siria

This program is based on program01.eng.py.

Approaching the problem by defining individual problems as functions
###0) crea un dizionario per i punteggi DONE in function tournament(matchlist)
###1) togliere gli spazi e i tab DONE in function removespaces(lst)
2) un paio di cicli per trovare le combinazioni possibili, 
   tipo in un gruppo di 3 giocatori sarebbero (0,1) (0,2) e (1,2).
3) per ogni combinazione devi:
- eseguire una funzione( o anche senza) per stabilire chi ha vinto.
  Le condizioni di vittoria sono nella prima parte del testo
  (devi confrontare le singole lettere dei due giocatori e assegnare un punto per lettera 
  a chi ha vinto).
- se hanno fatto gli stessi punti quindi pareggio, allora devi comparare la somma dei loro valori
  in ord e chi vince sta scritto nel testo.
4) sortare la classifica finale(se è un dizionario sorti le keys in base alle values)
"""

#part 1 : remove spaces from input list (by making a copy to avoid errors)
# THIS WORKS
def removespaces(lst):
    lstcopy = lst.copy()
    lstcopy = [x.replace(' ', '').replace('\t', '') for x in lstcopy]
    return lstcopy

#part 2 : do the tournament like structure for the list
# THIS DOESN'T WORK
def tournament(lstcopy):
    points = {} #defining an empty dictionary for the points
    for i in range(len(lstcopy)):
        for j in range(len(lstcopy)):
            print(lstcopy[i][i], lstcopy[j][i])
            
            
            
'''output we want is (with ['abc','def','ghi'])
a d 
a g
d g
b e     
b h
e h
c f
c i
f i
#a a MISSING  d g 1,0 2,0
              a d 0,0 1,0
              a g 0,0 2,0
              e b 1,1 0,1
#e e MISSING  b h 0,1 2,1
              e h 1,1 2,1
              i c 2,2 0,2
              i f 2,2 1,2
#i i MISSING  c f 0,2 1,2
'''
    

