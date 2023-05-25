def es36(listaDizionari):
    '''
    Si implementi la funzione es36(listaDizionari) che presi in input una lista di dizionari
    restituisce un dizionario.
    I dizionari in input della listaDizionari hanno come chiave stringhe
    di caratteri tra 'a' e 'z' e come attributo liste di interi.
    Il dizionario restituito deve avere le chiavi che risultano presenti in tutti i dizionari della listaDizionari.
    A ciascuna chiave x di questo dizionario e' associata una lista di interi.
    Un intero e' presente nella lista se e solo se e' presente in tutte le liste di attributi della chiave x.
    La lista deve risultare ordinata in modo crescente.

    Ad esempio se la listaDizionari contenente i tre dizionari
    {'a': [1,3,5],'b':[2,3],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    il dizionario restituito sara' {'a':[3,5],'d':[]}
    '''
    # inserisci qui il tuo codice
    res = {}
    keys = [set(d.keys()) for d in listaDizionari]
    
    keys_i = intersection_r(keys)
    
    for key in keys_i:
        values = intersection([set(d[key]) for d in listaDizionari])
        res[key] = list(values)
    
    return res
    
def intersection(lst):
    if len(lst) == 0: return set()
    lset = lst[0]
    
    for l in range(1,len(lst)):
        lset = lset & lst[l]
        
    return lset

def intersection_r(lst): # fa interz lista di set
    if len(lst) == 0: return set()
    if len(lst) == 1: return lst[0]
    #if len(lst) == 2: return set(lst[0]) & set(lst[1])
    return lst[0] & intersection_r(lst[1:])

def union_r(lst):
    if len(lst) == 0: set()
    if len(lst) == 1: return lst[0]
    return lst[0] | lst[1] | union_r(lst[2:])