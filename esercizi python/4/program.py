import immagini


def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    
    - legge l'immagine da fimm e crea una seconda  immagine
    
    - L'immagine da creare ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h 
      e ampiezza w aventi tutti il colore del pixel originario.
      
    - salva l'immagine creata all'indirizzo fimm.
    
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
      caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
      
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    #scrivi qui il tuo codice
    image = immagini.load(fimm)
    image2 = [[0 for x in range(len(image[0]))] for y in range(len(image))]
    newpix = []
    
    for row in range(len(image)):
        for pix in range(len(image[0])):
            newpix.append(image[row][pix] * h1 * w1) 
            
    return image2
    
if __name__ == '__main__':
    es4('cubo.png', 'a.png', 2, 2)