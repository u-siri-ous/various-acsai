def es16(s, k):
    '''
    Es 5: 3 punti
    progettare la funzione es16(s,k) che: 
    - riceve  in input una stringa s di caratteri ed un intero k 
    - costruisce la lista con  le diverse sottostringhe  di s  in cui compaiono 
      esattamente k caratteri distinti
    - restituisce la lista delle sottostringhe dopo averla ordinata  per
      lunghezze decrescenti e, a parita' di lunghezza, in ordine lessicografico
   Nota che la lista non deve contenere duplicati.
   Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
   caratteri iniziali  e 0 o piu' caratteri finali.
   ESEMPI: 
   con s='aabbb' e k=1 la funzione restituisce la lista ['bbb', 'aa', 'bb', 'a', 'b']
   con s='bcafedg' e k=3 la funzione restituisce la lista ['afe', 'bca', 'caf', 'edg', 'fed']
   con s='ccaabbdd' e k=3 la funzione restituisce la lista 
                          ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']
    '''
    lset = distinct(s)
    sub = []
    
    if lset == len(s):
        sub = [s[i:i+k] for i in range(len(s)-k+1)] #sottostringhe k elementi in una stringa di tutti caratteri distinti
        sub.sort()
        return sorted(sub, key = lambda x : len(x), reverse=True)
        
    for i in range(len(s)):
        for j in range(i+k,len(s)+1):
            if distinct(s[i:j]) == k and s[i:j] not in sub:
                sub.append(s[i:j])
    
    sub.sort()
    return sorted(sub, key = lambda x : len(x), reverse=True)
        
def distinct(s):
    return len(set(s)) #how many distinct characters in a string s