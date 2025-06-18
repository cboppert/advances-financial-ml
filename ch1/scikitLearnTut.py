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

# Let's do some plotting!
import matplotlib.pyplot as plt

fig, ax = plt.subplots(ncols=2, figsize=(10, 5), sharex=True, sharey=True)

ax[0].scatter(X_train, y_train, label="Train data points")
ax[0].plot(
    X_train,
    regressor.predict(X_train),
    linewidth=3,
    color="tab:orange",
    label="Model Prediction"
)
ax[0].set(xlabel="Feature", ylabel="Target", title="Train set")
ax[0].legend()

ax[1].scatter(X_test, y_test, label="Test data points")
ax[1].plot(X_test, y_pred, linewidth=3, color="tab:orange", label="Model predictions")
ax[1].set(xlabel="Feaure", ylabel="Target", title="Test set")
ax[1].legend()

fig.suptitle("Linear Regression")
plt.show()

# Ordinary Least Squares and Ridge Regression Variance
import numpy as np
from sklearn import linear_model

X_train2 = np.c_[0.5, 1].T
y_train2 = [0.5, 1]
X_test2 = np.c_[0, 2].T

np.random.seed(0)

classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)

for name, clf in classifiers.items():
  fig2, ax2 = plt.subplots(figsize=(4, 3))

  for _ in range(6):
    this_X = 0.1 * np.random.normal(size=(2, 1)) + X_train2
    clf.fit(this_X, y_train2)

    ax2.plot(X_test2, clf.predict(X_test2), color="gray")
    ax2.scatter(this_X, y_train2, s=3, c="gray", marker="o", zorder=10)

  clf.fit(X_train2, y_train2)
  ax2.plot(X_test2, clf.predict(X_test2), linewidth=2, color="blue")
  ax2.scatter(X_train2, y_train2, s=30, c="red", marker="+", zorder=10)

  ax2.set_title(name)
  ax2.set_xlim(0, 2)
  ax2.set_ylim(0, 1.6)
  ax2.set_xlabel("X")
  ax2.set_ylabel("y")

  fig.tight_layout()

plt.show()
