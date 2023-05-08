import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris = sns.load_dataset("iris") #loading the "iris" flower dataset
sns.set()

#tables are set up with pandas

#sns.pairplot(iris, hue="species", height=1.5) #divide samples by species
#plt.show(block=True) #show the plots divided by species
#print(iris.shape)

#delete the table column from the dataset
X_iris = iris.drop("species", axis=1) #remove all rows from column 1
#print(X_iris.shape)

#create the list containing the labels: it gets the column and it stores it in the varible
y_iris = iris["species"]
#print(y_iris.shape)


#how to train a model with scikit-learn?
# 1 - import appropriate module, each set of algos belongs to a bigger set (clustering, regression etc)
# 2 - we need to specify hyperparameters, parameters that are initialized before the model training.
#	  the model cannot tune them, they are set previously by the programmer. The learning rate is a hyperparameter.
# 3 - prepare the data, such as x containing data, y containing labels
# 4 - we need a fit function: it trains the data


#naive Bayes classifier is a ml classifier that exploits conditional probability: given features,
#computes probability of the class
#assuming the sample follows a gaussian distribution, it maximises the correct assignation of the class


#split the dataset into training set(to train model) and test set(to check if it's trained well)
#takes as an input all the labels, shuffles the dataset and splits it
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,train_size=0.7) 

#instantiate the model
model = GaussianNB()

#train the model
model.fit(Xtrain,ytrain)

#check if models are correctly classified: do the prediction 
y_pred = model.predict(Xtest)

#check how good our model is: we compare predicted labels with correct ones
accuracy  = accuracy_score(ytest,y_pred)

print(accuracy)