import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

class LinearRegressionClosed:

    def __init__(self):
        self.coef_ = None       #m
        self.intercept_ = 0.0   #b

    def fit(self, x, y):
        X = np.array(X)
        y = np.array(y)

        Xb = np.c_[np.ones((X.shape[0], 1)), X]

        A = np.linalg.inv(X.T @ Xb) @ Xb.T @ y
        self.intercept_ = A[0]
        self.coef_ = A[1:]


    def predict(self, x):
        X = np.array(X)

        return X @ self.coef_ + self.intercept_
    
reg = LinearRegressionClosed()

X, y = fetch_california_housing(return_X_y=True)
reg.fit(X,y)

y_pred = reg.predict(X)
print(r2_score(y, y_pred))
