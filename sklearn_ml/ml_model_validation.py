from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# load dataset
iris = load_iris()

X = iris.data       # data (matrix)
y = iris.target     # labels (vector)

# pick a model 
model = KNeighborsClassifier(n_neighbors=1)     

# train model 
model.fit(X,y)

# do the prediction (test)
y_pred = model.predict(X)

# compute accuracy
accuracy = accuracy_score(y, y_pred)    

# both training and testing model only on X gives overfitting
# use cross-validation in order to avoid this (details in slides)

# step 1: split dataset, create training and testing datasets
X1, X2, y1, y2 = train_test_split(X, y, train_size=0.5)

# step 2: train models
model1 = model.fit(X1, y1)
model2 = model.fit(X2, y2)

# step 3: do predictions, swapping the models for cross-validation
y1_pred = model1.predict(X2)
y2_pred = model2.predict(X1)

# step 4: finally, compute accuracies, also swapping models
accuracy1 = accuracy_score(y2, y1_pred)    
accuracy2 = accuracy_score(y1, y2_pred)     # è una merda, però vabbè (problem of ovefitting)

# step 5: decide how we wanna get accuracy (here, we use the mean)
accuracy_mean = (accuracy1+accuracy2)/2

print(accuracy_mean)