from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.corpus

'''
Chunking - identify phrases
uses POS tagging, unlike tokenizing
'''
lotr = "It's a dangerous business, Frodo, going out your door."

#1) tokenize for POS
words = word_tokenize(lotr)

#2) tag the words (automatically, uses a neural network)
lotr_pos = nltk.pos_tag(words)

my_string = "NP: {<DT>?<JJ>*<NN>}"      #regexp
# it means "extract all":
# NP    "noun phrases
# DT    with determiners
# ?     optionally present (? stands for optional quantity (in regexp))
# JJ    and adjectives
# *     in any number, 
# NN    ending with a noun"

chunk_parser = nltk.RegexpParser(my_string)

tree = chunk_parser.parse(lotr_pos)

#draw the relationship between words and their label and finds minimal phrases specified in the regexp
tree.draw()