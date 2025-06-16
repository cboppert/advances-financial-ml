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

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1,1], [2, 2]], [0, 1, 2])


