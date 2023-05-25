import os
import os.path


def es67(path):
    """
    ATTENZIONE: e' VIETATO usare la funzione os.walk o altre funzioni di libreria che 
    permettono di cercare tutti i file presenti in una directory. 
    (la directory la dovete esplorare voi)

    Si definisca la funzione ricorsiva (o che fa uso di vostre funzioni ricorsive) es67 che:
    - riceve come argomento un path del filesystem
    - esplora ricorsivamente la directory corrispondente e torna un dizionario.

    NOTA: tutti i file e directory che iniziano con '.' vanno ignorati.

    Il dizionario ha come chiave le estensioni dei file trovati nella directory 
    (ovvero gli ultimi 3 caratteri del nome dei file, es: 'txt', 'pdf', 'png').
    Il valore associato a ciascuna chiave K e' la distanza (differenza delle profondita')
    tra il piu' profondo file che ha quella estensione e il meno profondo.
    Assumete che i file contenuti nella directory path siano a profondita' 0.
    Esempio:
    se nella directory con path='A1' sono presenti i soli due file di tipo 'txt'
        A1/a/b/c/d/e/f/g/h/pippo.txt    a profondita' 8    (contando A1 = 0)
        A1/d/f/pappo.txt                a profondita' 2
        risultato contiene la coppia chiave: valore
        'txt' : 6
    """
    dic = {}
    file = depth(path, dic, 0)
    
    for key in dic.keys():
        m = min(dic[key])
        M = max(dic[key])
        dic[key] = M-m
    
    return dic

def depth(path, dic, d):
    
    for f in os.listdir(path):
        
        if os.path.isdir(path + '/' + f):
            depth(path + '/' + f, dic, d+1)
            
        elif os.path.isfile(path + '/' + f) and not f.startswith('.'):
            file = os.path.splitext(f)
            if dic.get(file[1][1:]) is None:
                dic[file[1][1:]] = []
            dic[file[1][1:]].append(d)
            
    return

if __name__ == '__main__':
    depth('./A1',{},0)