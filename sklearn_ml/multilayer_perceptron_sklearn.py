from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml, load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# implementation of ANNs (RNN and CNN)
# neurons and perceptrons
# how does a neuron learn? stochastic gradient descent(sgd), we aim to find the set of weights that minimizes the error 
# through forward and back propagation
# ANNs as graphs

""" import ssl
ssl._create_default_https_context = ssl._create_unverified_context 
# if you get the urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)> error """

# MNIST dataset - handdrawn digits 0-9 in 28x28 grayscale images
# download dataset, return training data and labels split
# X, y = load_digits(return_X_y=True)   
X, y = fetch_openml('mnist_784', return_X_y=True, parser="auto")   # funziona ma ci mette un botto, parser="auto" messo sennò se impunta ed è finita

# create train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)       

# create the model
model = MLPClassifier(hidden_layer_sizes=(20, ), verbose=True)    # default solver is adam, 20 neurons in the 1st hidden layer

# train the model
model.fit(X_train, y_train)

# check accuracy for the model (test the model)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)