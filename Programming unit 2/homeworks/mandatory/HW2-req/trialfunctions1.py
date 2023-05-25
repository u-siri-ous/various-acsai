# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:16:21 2021

@author: Siria

This program is based on program01.eng.py.

Approaching the problem by defining individual problems as functions
0) crea un dizionario per i punteggi
1) togliere gli spazi e i tab
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
def sum_points(match):
    list1 = [] 
    list2 = []
    for i in match:
        list1 = []
        for j in i:
            u = 0
            j = ord(j)
            list1.append(j)
            if len(list1) == len(i):
                u = sum(list1)
                list2.append(u)
    return list2

def ex(matches, k):
    
    match = matches.copy()
    match = [x.replace(' ', '').replace('\t', '') for x in match] #removing spaces and tabs
    
    pointsA = 0
    pointsB = 0
    points = {}
    playsum = sum_points(match)
# =============================================================================
#     for i in match:
#         match = [ord(x) for x in match]
#         playsum += [sum(i)]
# =============================================================================
    for i in range(len(match)):
        for j in range(i+1, len(match)):
            for c in range(len(match[i])):
                sub = ord(match[i][c]) - ord(match[j][c])
                if sub <= k: #difference less than k
                    if (ord(match[i][c]) > ord(match[j][c])):
                        pointsA += 1
                    elif (ord(match[i][c]) < ord(match[j][c])):
                        pointsB += 1
                        
                elif sub > k: #difference bigger than k
                    if (ord(match[i][c]) > ord(match[j][c])):
                        pointsB += 1
                    elif (ord(match[i][c]) < ord(match[j][c])):
                        pointsA += 1
                        
            if pointsA == pointsB: #tie
                if playsum[i] > playsum[j]:
                    pointsA += 1
                elif playsum[i] < playsum[j]:
                    pointsB += 1
                else:
                    if ord(match[i]) < ord(match[j]):
                        pointsA += 1
                    else:
                        pointsB += 1
                            
    #return sorted(range(len(points)), key=lambda k: points[k], reverse=True)

if __name__ == "__main__":
    
    tests=[
            {'k':2,  'matches':["aac","ccc","caa"], 'result':[1,0,2]},
            {'k':1,  'matches':["aac","ccc","caa"], 'result':[0,2,1]},
            {'k':10, 'matches':["abc","dba","eZo"], 'result':[0,1,2]},
            {'k':50, 'matches':["A ƐÈÜ","BEAR","c Ʈ  ´  ."], 'result':[1,2,0]}
            ]

    for  test in tests:
        result =  ex(test['matches'], test['k'])
        if result == test['result']:
            print("OK")
        else:
            print("FAIL")
    

