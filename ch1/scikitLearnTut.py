# pip install -U scikit-learn

# Wow you could just run through this documentation for a great overview of the field
# https://scikit-learn.org/stable/modules/linear_model.html

## Supervised Learning

## predictedValue(vectorW, vectorX) := w0 + w1x1 + ... + wNxN
    # vectorW is coef_
    # w0 is intercept_

### Linear Regression

### Ordinary Least Squares

    # Fits linear model with coeficients w = w1, ..., wP
    # Minimize residual sum of squares between observed targets in dataset and targets predicted by linear approximation
    # Relies on independence of features
    # Multicolinearity occurs when columns have approximate linear dependence... may occur when data collected without experimental design

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit([[0, 0], [1,1], [2, 2]], [0, 1, 2])

## Let's do the Ordinary Least Squares and Ridge Regression
## tutorial here 
## https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#sphx-glr-auto-examples-linear-model-plot-ols-ridge-py
##
## Has plotting!

from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X = X[:, [2]] # Use only one feature
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, shuffle=False)

# Create a linear regression model and fit on data
regressor = LinearRegression().fit(X_train, y_train)

# Predict Performance
y_pred = regressor.predict(X_test)

print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Coefficient of determination: {r2_score(y_test, y_pred):.2f}")
