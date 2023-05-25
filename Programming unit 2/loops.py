#program to try out while loops

import random

def guessmyage(v):
    x = random.randint(0,v)
    question = "guess my age: "
    guess = int(input(question))
    while guess != x:
        print("F")
        guess = int(input(question))
    print("yay")
