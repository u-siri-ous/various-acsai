from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

""" import nltk
nltk.download("punkt")    #one time thing, came out in an error
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger") """

#extract wanted information from strings using regexp!!
'''
punkt knows how to spit the sentence
sent_tokenize uses stopwords, a list of words that tess it where to split

nltk is language sensitive

stopwords are words that are so common they are basically ignored by typical tokenizers

The stopwords in nltk are the most common words in data
They are words that you do not want to use to describe the topic of your content
They are pre-defined and cannot be removed
'''
ex = "quel ramo sul lago di como che volge a mezzogiorno"

sent_t = sent_tokenize(ex)      #will split at '.'
word_t = word_tokenize(ex)      #will split at ' ', punctuation count as words

#using stopwords
quote = "it's leviosa, not leviosaaaa"
word_quote = word_tokenize(quote)

stop_words = set(stopwords.words("english"))

filtered_words = []

for word in word_quote:
    if word.casefold() not in stop_words:   #removing case-sentitivity
        filtered_words.append(word)

print(filtered_words)

#content vs context words