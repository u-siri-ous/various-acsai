def es51(ls, c):
    '''
    progettare la funzione es51(ls,c) che: 
    - riceve  in input una lista di parole ls ed un carattere c
    - cancella da ls le parole che contengono il carattere c (sia in maiuscolo che in minuscolo)
    - restituisce il numero di parole cancellate da ls. 
    Nota che al termine della funzione la lista passata come parametro deve risultare modificata
    (ricorda che le liste sono mutabili). 
     ESEMPI:
     Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio','Luca', 'Ugo'] e c='a'
     la funzione restituisce 5 e la lista ls diventa ['Lucio','Ugo']  
     Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca','Ugo'] e c='G'
     la funzione restituisce 2 e la lista ls diventa ['Andrea', 'Fabio', 'Francesco', 'Lucio','Luca']
    '''
    count = 0
    i = 0
    
    while i < len(ls):
        if c.lower() in ls[i].lower():
            del ls[i]
            count += 1 
        else : i += 1
    
    return count

if __name__ == '__main__':
    es51(['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'], 'a')