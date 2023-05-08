import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# regression - study the trend of the data
# initialize the seed
rng = np.random.RandomState(42)

# create fake (placeholder/starter) data, in xy coordinates
x = 10 * rng.rand(50)
y = 2 * x-1 * rng.rand(50)

# pick the model we wanna use - since we're doing linear regression, we use it
model = LinearRegression(fit_intercept=True)    # hyperparameter: used to LEARN and cannot be learned

# we reshape the data in form of matrix
X = x[:, np.newaxis]

# train model
model.fit(X, y)

# create test data
x_fit = np.linspace(-1,11)  # creates an evenly spaced array of values
X_fit = x_fit[:, np.newaxis]    # matrix form

# learn how to predict labels for new data
y_pred = model.predict(X_fit)

# see predictions
plt.scatter(x,y)
plt.plot(X_fit, y_pred) 
plt.show()