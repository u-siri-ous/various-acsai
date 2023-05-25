#basic mastermind game initials: (R,B,Y,G,P,O)

def comparesequence(correctseq, guessseq):
    blackpeg = 0
    whitepeg = 0
    if len(correctseq) == len(guessseq):
        for element1 in guessseq:
            for element2 in correctseq:
                if element1 == element2:
                    blackpeg += 1
                #elif element1 in element2 and element1 != element2: #not working :c
                    #whitepeg +=1               
        print("black pegs are: ", blackpeg)
        print("white pegs are: ", whitepeg)
    else:
        print("plz equal length")
    return blackpeg, whitepeg
    
#professor correction

def professorcorr(correctseq, guessseq):
    blackpeg = 0
    whitepeg = 0
    guesscount = 0
    for ccolor in correctseq:
        if ccolor == guessseq[guesscount]: #counter var must be int
            blackpeg += 1
            correctseq[guesscount] = '-'
            guessseq[guesscount] = '*'
        guesscount += 1
    for gcolor in guessseq:
        correctcount = 0
        for ccolor in correctseq:
            if gcolor == ccolor:
                whitepeg += 1
            correctcount += 1
    return blackpeg

if __name__ == "__main__":
    correctseq = ['r','y','o','b']
    guessseq = ['r','p','g','o']
    blackpeg, whitepeg = professorcorr(correctseq, guessseq)
    print(correctseq, guessseq, blackpeg, whitepeg)


    
