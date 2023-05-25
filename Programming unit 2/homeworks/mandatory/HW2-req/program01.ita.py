# -*- coding: utf-8 -*-
'''Nel gioco "chi la spara più grossa" si sfidano due concorrenti A e
B che generano delle sequenze di valori di lunghezza variabile,
rappresentati da un singolo carattere. Le sequenze possono essere di
lunghezza diversa poiché i valori possono essere separati da uno (o
più) spazi bianchi e tab ('\t'). Il numero di caratteri non spazio è,
comunque, uguale per ogni sequenza.

Ogni elemento della sequenza di A viene confrontato con l'elemento
corrispondente della sequenza di B e viene assegnato un punto
- al concorrente che ha generato il valore più alto (per esempio A),
  se la differenza fra il valore di A e il valore di B è inferiore o
  uguale ad un parametro k deciso all'inizio della sfida
- al concorrente che ha generato il valore più basso (per esempio B),
  se la differenza fra il valore di A e il valore di B è superiore
  a k (cioè A ha sballato)
- a nessuno, in caso di pareggio.
Al termine dell'assegnazione, vince chi ha ottenuto più punti. In caso
di pareggio, vince il giocatore che ha generato la sequenza con somma
totale dei valori inferiore.  In caso di ulteriore pareggio, il punto
è assegnato al giocatore con la prima sequenza in ordine
lessicografico. Non può capitare che due giocatori generino
esattamente la stessa sequenza di valori.

Si deve realizzare una funzione che prende in input il parametro k e
una lista di stringhe corrispondenti a un torneo di "chi la spara più
grossa" e restituisce la classifica finale del torneo. La stringa in
posizione i corrisponde alla sequenza dei valori generati dal
giocatore i.

Nel torneo, ogni giocatore sfida tutti gli altri con la propria
sequenza: ovvero, se ci sono n giocatori, ogni giocatore farà n-1
sfide. Il numero di sfide vinte determina la posizione in
classifica. In caso di parità di sfide vinte, i giocatori sono
ordinati in modo crescente in base alla posizione.

Esempio di partite a chi la spara più grossa fra tre giocatori.
    Se k=2 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2.
        Alla fine 0 ha 1 sfida, 1 ha 2 sfide e 2 ha 0 sfide, per cui
            la classifica finale sarà [1, 0, 2].

    Se k=1 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 0 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 2 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        Alla fine 0 ha 2 sfide, 1 ha 0 sfide e 2 ha 1 sfida, per cui
            la classifica finale sarà [0, 2, 1].

    Se k=10 e la lista è  [ "abc",  "dba" , "eZo"]
        La sfida 0, 1 è un pareggio, ma vince 0 perché la sua sequenza
            ha somma inferiore.
        La sfida 0, 2 è vinta da 0 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'c'.
        La sfida 1, 2 è vinta da 1 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'a'
        Alla fine 0 ha 2 sfide, 1 ha 1 sfida e 2 ha 0 sfide, per cui
            la classifica finale sarà [0, 1, 2].

    Se k=50 e la lista è  [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        La sfida 0, 1 è vinta da 1 per 4 punti a 0.
        La sfida 0, 2 è vinta da 2 per 3 punti a 1.
        La sfida 1, 2 è vinta da 1 per 3 punti a 1.
        Alla fine 0 ha 0 sfide, 1 ha 1 sfida e 2 ha 2 sfide, per cui
        la classifica finale sarà [1, 2, 0].

Il timeout per l'esecuzione di ciascun test è di 6 secondi (*2 sualla VM)

'''

def player_sum(player):
    
    pl_value = 0
    
    for i in player:
        pl_value += i
        
    return pl_value

def match_ord(match):
    
    l = []
    
    for i in match:
        l1 = []
        for j in i:
            l1.append(ord(j))
        l.append(l1)
    
    return l

def ex(matches, k):
    
    match = matches.copy()
    match = [x.replace(' ', '').replace('\t', '') for x in match] #removing spaces and tabs
    
    match = match_ord(match)
    
    pointsA = 0
    pointsB = 0

    playsum = [-1] * len(match)
    total_points = list(map(lambda x: x*0, playsum))
    
    for i in range(len(match)-1):        
        for j in range(i+1, len(match)):
            pointsA, pointsB = 0,0
            for c in range(len(match[i])):
                sub = abs(match[i][c] - match[j][c])
                
                if sub == 0:
                    pass
                
                elif sub <= k:
                    if match[i][c] > match[j][c]:
                        pointsA += 1
                    else:
                        pointsB += 1
                        
                else:
                    if match[i][c] > match[j][c]:
                        pointsB += 1
                    else:
                        pointsA += 1
                    
            if pointsA > pointsB:
                total_points[i]+= 1
                
            elif pointsB > pointsA:
                total_points[j]+= 1
                
            elif  pointsA == pointsB:
                
                if playsum[i] == -1:
                    playsum[i] = player_sum(match[i])
                if playsum[j] == -1:
                    playsum[j] = player_sum(match[j])
                
                if playsum[i] < playsum[j]:
                    total_points[i]+= 1
                    
                elif playsum[i] > playsum[j]:
                    total_points[j]+= 1
                    
                elif playsum[i] == playsum[j]:
                    if match[i] < match[j]:
                        total_points[i] += 1
                    else:
                        total_points[j] += 1
                        
    return sorted(range(len(total_points)), key = lambda index : total_points[index], reverse = True)

# =============================================================================
# def sum_points(players):
#     
#     list2 = []
#     
#     for i in players:
#         pl_value = 0
#         for j in i:
#             pl_value += j
#         list2.append(pl_value)
#     return list2
# 
# def match_ord(match):
#     l = []
#     
#     for i in match:
#         l1 = []
#         for j in i:
#             l1.append(ord(j))
#         l.append(l1)
#     
#     return l
# 
# def ex(matches, k):
#     
#     match = matches.copy()
#     match = [x.replace(' ', '').replace('\t', '') for x in match] #removing spaces and tabs
#     
#     match = match_ord(match)
#     
#     pointsA = 0
#     pointsB = 0
# 
#     playsum = sum_points(match)
#     total_points = list(map(lambda x: x*0, playsum))
#     
#     for i in range(len(match)-1):        
#         for j in range(i+1, len(match)):
#             pointsA, pointsB = 0,0
#             for c in range(len(match[i])):
#                 sub = abs(match[i][c] - match[j][c])
#                 
#                 if sub == 0:
#                     pass
#                 
#                 elif sub <= k:
#                     if match[i][c] > match[j][c]:
#                         pointsA += 1
#                     else:
#                         pointsB += 1
#                         
#                 elif sub > k:
#                     if match[i][c] > match[j][c]:
#                         pointsB += 1
#                     else:
#                         pointsA += 1
#                     
#             if pointsA > pointsB:
#                 total_points[i]+= 1
#                 
#             elif pointsB > pointsA:
#                 total_points[j]+= 1
#                 
#             elif  pointsA == pointsB: 
#                 if playsum[i] < playsum[j]:
#                     total_points[i]+= 1
#                     
#                 elif playsum[i] > playsum[j]:
#                     total_points[j]+= 1
#                     
#                 elif playsum[i] == playsum[j]:
#                     if match[i] < match[j]:
#                         total_points[i] += 1
#                     else:
#                         total_points[j] += 1
#                         
#     return sorted(range(len(total_points)), key = lambda index : total_points[index], reverse = True)
# 
# =============================================================================

# =============================================================================
# def sum_points(players):
#     
#     list2 = []
#     
#     for i in players:
#         pl_value = 0
#         for j in i:
#             pl_value += ord(j)
#         list2.append(pl_value)
#     return list2
# 
# def ex(matches, k):
#     
#     match = matches.copy()
#     match = [x.replace(' ', '').replace('\t', '') for x in match] #removing spaces and tabs
#     
#     pointsA = 0
#     pointsB = 0
# 
#     playsum = sum_points(match)
#     total_points = list(map(lambda x: x*0, playsum))
#     
#     for i in range(len(match)-1):        
#         for j in range(i+1, len(match)):
#             pointsA, pointsB = 0,0
#             for c in range(len(match[i])):
#                 sub = abs(ord(match[i][c]) - ord(match[j][c]))
#                 
#                 if sub == 0:
#                     pass
#                 
#                 elif sub <= k:
#                     if ord(match[i][c]) > ord(match[j][c]):
#                         pointsA += 1
#                     else:
#                         pointsB += 1
#                         
#                 elif sub > k:
#                     if ord(match[i][c]) > ord(match[j][c]):
#                         pointsB += 1
#                     else:
#                         pointsA += 1
#                     
#             if pointsA > pointsB:
#                 total_points[i]+= 1
#                 
#             elif pointsB > pointsA:
#                 total_points[j]+= 1
#                 
#             elif  pointsA == pointsB: 
#                 if playsum[i] < playsum[j]:
#                     total_points[i]+= 1
#                     
#                 elif playsum[i] > playsum[j]:
#                     total_points[j]+= 1
#                     
#                 elif playsum[i] == playsum[j]:
#                     if match[i] < match[j]:
#                         total_points[i] += 1
#                     else:
#                         total_points[j] += 1
#                         
#     return sorted(range(len(total_points)), key = lambda index : total_points[index], reverse = True)
# 
# =============================================================================

if __name__ == "__main__":
    pass
    # Inserisci qui i tuoi test
