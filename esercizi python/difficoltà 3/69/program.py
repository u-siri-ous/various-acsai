import os
import os.path
"""
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
    che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
    solo se si trovano alla profondita' indicata, e che riceve come argomenti:
        
        dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
        
        profondita: la profondita' in cui dobbiamo cancellare i file, 
                    contando da 0 per la directory radice passata come argomento
                    
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
        
    La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore o uguali 
    a 'profondita', che NON sono stati cancellati

    NOTA: ignorate tutti i file e directory che iniziano con '.'

    NOTA: per eliminare un file usate la funzione os.remove

    Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', si chiama la funzione 
           e si controlla che i file contenuti nelle directories esistano/non esistano a seconda del caso 
           (senza usare una soluzione ricorsiva ma testando direttamente i path dei files relativi alla dir iniziale)
           
    Test: che la funzione sia ricorsiva
"""

def es69(dir, profondita, estensioni):
    cf = [0]
    countfile = indepth(dir, profondita, estensioni, 0, cf)
    return countfile[0]

def indepth(dr, d, ext, current, countfile):
    
    for f in os.listdir(dr):
        if not f.startswith('.'):
            
            if os.path.isdir(dr + '/' + f):
                indepth(dr + '/' + f, d, ext, current+1, countfile)
            
            elif os.path.isfile(dr + '/' + f):
                s = os.path.splitext(dr + '/' + f)[1][1:]
                
                if s in ext and current == d:
                    os.remove(dr + '/' + f)
                        
                elif current <= d:
                    countfile[0] += 1  
                
    return countfile
                
if __name__ == '__main__':
    es69('t2', 3, ['jpg', 'png'])