from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.corpus

'''
Stemming is the process of producing morphological variants of a root/base word
Stemming programs are commonly referred to as stemming algorithms or stemmers
A stemming algorithm reduces the words “retrieval”, “retrieved”, “retrieves” to the stem “retrieve"
'''
stemmer = PorterStemmer()       #algo for stemming

ex = "trentatre trentini entrarono a trento tutti e trentatre trotterellando"

words = word_tokenize(ex)

#apply stemmer on each word to find root
stemmed = [stemmer.stem(word) for word in words]

'''
POS tagging, assign a label to each word (Part Of Speech), involves tokenizing
What do the labels mean? Download tagsets and call nltk.help.upenn_tagset() or look on nltk.org
'''
dijkstra = "Computer Science is no more about computers than astronomy is about telescopes"
words = word_tokenize(dijkstra)

#POS tagging of sentences
result = nltk.pos_tag(words)

'''
Lemmatizing is similar to stemming, but it gets the core meaning of the words
e.g. scarves -> scarf (returns the singular in this case)
It's more difficult as it needs a dictionary like structure
Doesn't work for EVERY word, in that case we have to specify the type of the word

With stemming, I would get "scarv"
'''
lemmatizer = WordNetLemmatizer()

#result = lemmatizer.lemmatize("scarves")
result = lemmatizer.lemmatize("worst", pos="a")     #worst is an adjective

print(result)

'''
Homograph in NLP, when the meaning of a word is ambiguous
like pesca - frutto, pesca - attività
'''