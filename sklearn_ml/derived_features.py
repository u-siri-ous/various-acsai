import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# derived features are really discriminative: (extracting features from other features)
# e.g. we need to analyze the movement of a player, we extract the joints, and the joint is a feature 

# create data
x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

X = x[:, np.newaxis]

#model = LinearRegression().fit(X,y)        # underfitting ewwww
#y_pred = model.predict(X)

# we can use derived features to split data and enhance number of features for each dimension of the data
poly = PolynomialFeatures(degree=3)
X2 = poly.fit_transform(X)

# Polynomial features
# Generate a new feature matrix consisting of all polynomial combinations 
# of the features with degree less than or equal to the specified degree 
# in this case, it creates a matrix with each row [x^0, x^1, x^2, x^3] 
# in order to have more features and fit the data better

print(X2)

# a linear regressor that fits the data better
model = LinearRegression().fit(X2,y)
y_pred = model.predict(X2)

plt.scatter(x,y)
plt.plot(x, y_pred)
#plt.show()