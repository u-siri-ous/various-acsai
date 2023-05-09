# cope with mangled/missing data
from numpy import nan
import numpy as np
from sklearn.impute import SimpleImputer

# suppose that our X is:
X = np.array(
    [[nan, 0, 3],
     [3, 5, 2],
     [7, 9, nan]]
    )
y = np.array([14,16,8])     #training with X gives errors as nan is not a number, i.e. missing

# use simpleimnputer to fill missing data *in some way*
imputer = SimpleImputer(strategy='mean')      # fill according to column mean
X2 = imputer.fit_transform(X)

print(X2)