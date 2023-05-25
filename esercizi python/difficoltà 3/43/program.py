
def es43(ftesto):
    '''
    Si progetti la funzione es43(ftesto) che, preso in input l'indirizzo di un file di testo
    contenente righe contenenti interi separati da spazi, restituisce una lista  di interi.
    La lunghezza della lista e' data dal numero massimo di interi che compaiono nelle righe
    del file. E nella generica posizione i della lista c'e' l'intero corrispondente alla somma di tutti
    gli interi presenti in posizione  i  nelle varie righe che contengono almeno i interi.
    Ad esempio per il file contenente le  3 righe:
    ' 0 2  4
      6 8 10
      4 0  1'
    la funzione restituisce la lista [10,10,15] cioe' le somme in colonna
    Per il file contenente le  4 righe (nota, di lunghezza diversa):
    ' 1 2 3
      4 5 6 7 3 6
      1
      1 2'
    la funzione restituisce la lista [7,9,9,7,3,6] cioe' le somme in colonna
    '''
    with open(ftesto) as f:
        numbers = [[int(x) for x in n.split()] for n in f.readlines()]
        f.close()
        
    max_n = len(max(numbers, key=len))
        
    mat = [[0 for x in range(max_n)] for y in range(len(numbers))] 
    
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            mat[i][j] = numbers[i][j]
            
    lst = [sum([mat[i][j] for i in range(len(mat))]) for j in range(len(mat[0]))]
    
    return lst
        
if __name__ == '__main__':
    es43('finteri2.txt')