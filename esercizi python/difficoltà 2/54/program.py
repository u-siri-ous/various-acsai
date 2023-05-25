

import copy

def es54(lista):
    ''' 
    la funzione es54(lista) che presa in input una lista contenente interi e stringhe, modifica 
    la lista distruttivamente e restituisce un dizionario.
    Al termine della funzione dalla lista devono risultare  cancellate tutte le stringhe e il dizionario 
    restituito deve contenere come chiavi le stringhe cancellate ciascuna con attributo il numero di volte 
    in cui occorrevano nella lista.
    Ad esempio per lista=[1,'a',2,'b','a',8,'d',8] la funzione al termine restituisce il dizionario 
    {'a':2,'b':1,'d':1} e la lista diviene [1,2,8,8]
    '''
    # inserisci qui il tuo codice
    dic = {}
    for item in copy.copy(lista):
        #if isinstance(item, str) and item not in dic.keys():
            #dic[item] = lista.count(item)
            #lista = [i for i in lista if i != item]
        if isinstance(item, str):
            lista.remove(item)
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
    return dic