# import the dataset, recognition of text
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline      # create a pipeline of tasks to do 
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# select a subset od categories
categories = ['talk.religion.misc','sci.space', 'comp.graphics']

# load data
train = fetch_20newsgroups(subset='train', categories=categories)   # choose a training set from the categories chosen
test = fetch_20newsgroups(subset='test', categories=categories)

# how is a sample of data made? use slicing of lists
# print(train.data[5])

# we need to use TFIDF to weigh the words 

# create a model to use pipeline - an automatic sequence of operations
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)

labels = model.predict(test.data)

# confusion matrix usage - compute confusion matrix to evaluate the accuracy of a classification
mat = confusion_matrix(test.target, labels)

# how to read a confusion matrix:
# - on the main diagonal we have all the correctly classified things 
# - the rest are incorrectly classified (and as what) 

# plot confusion matrix
""" sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=train.target_names, yticklabels=test.target_names)
plt.xlabel('True labels')
plt.ylabel('Predicted labels')

plt.show() """

# try the classifier with our text
s = input()
pred = model.predict([s])

print(train.target_names[pred[0]])      # using prediction as index for training data to tell us in which category was s classified