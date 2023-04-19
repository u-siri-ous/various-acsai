#preprocessing on text
from nltk.tokenize import sent_tokenize, word_tokenize
#import nltk
#nltk.download('punkt ')    one time thing, came out in an error

'''
tokenizing (tokenizing a sentence): 
split a phrase in smaller parts, namely: 
1) tokenize by word
2) tokenize by sentence
'''

ex = "quel ramo sul lago di como. che volge a mezzogiorno"

sent_t = sent_tokenize(ex)      #will split at '.'
word_t = word_tokenize(ex)      #will split at ' '

print(sent_t, word_t)