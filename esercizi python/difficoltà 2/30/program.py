

def es30(fname1,fname2,fname3):
    ''' 
    Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
    Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
    sostituito da un intero di tre cifre.
    Tutti i caratteri non numerici devono essere trasferiti come sono.
    Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
    del testo e il rispettivo carattere. 
    Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
    presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
    Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
    sono necessariamente presenti nel file di decodifica.
    La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
    alle informazioni contenute nel secondo.
    I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
    Il messaggio decodificato va poi salvato nel terzo file.
    La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
    Ad esempio se 
    - il file fname1 contiene il testo '991118991991345      103    091027003091103?'
    - il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
    il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
    Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
    '''
    # inserisci qui il tuo codice
    mappa = {}
    with open(fname2, encoding='utf8') as f:
        for riga in f:
            c, n = riga.split()
            mappa[n] = c
    testo =''
    with open(fname1,encoding='utf8') as f:
        testo = f.read()
    testo1 = ''
    quanti = 0
    i = 0
    while i < len(testo):
        c = testo[i]
        if c in '0123456789':
            k = testo[i:i+3]
            i += 3
            if k in mappa:
                testo1 += mappa[k]
            else:
                testo1 += '?'
                quanti += 1
        else:
            i += 1
            testo1 += c
    with open(fname3, mode='w',encoding='utf8') as f:
        f.write(testo1)
    return quanti
            
            
            
            




















