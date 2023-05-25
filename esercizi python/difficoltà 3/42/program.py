
import immagini

def es42(fImageIn, fcolori, fImageOut):
    '''
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    '''
    colorsin, colorsout = pixels(fcolori)
    image = immagini.load(fImageIn)
    count = [0]
    
    image = [[change(pix, colorsin, colorsout, count) for pix in row] for row in image]
    
    immagini.save(image, fImageOut)
    
    return count[0]

def change(pix, colorsin, colorsout, count):
    
    if pix in colorsin:
        ind = colorsin.index(pix)
        pix = colorsout[ind]
        count[0] += 1
    
    return pix

def pixels(fcolori):
    with open(fcolori) as f:
        lista = f.read().split()
        colors = [(int(lista[i]), int(lista[i+1]), int(lista[i+2])) for i in range(0, len(lista), 3)]
        f.close()
        
    colorsin = [colors[i] for i in range(0, len(colors), 2)]
    colorsout = [colors[i] for i in range(1, len(colors), 2)]
            
    return colorsin, colorsout

if __name__ == "__main__":
    es42('scacchiera.png', 'fcolori1.txt', 'a.png')