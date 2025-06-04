# Numpy - https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np

# why use Numpy

## Python lists are excellent fast general purpose heterogenous containers

## However, NumPy shines when processing large amount of homogenous data by using appropriate data structures to reduce memory consumption and boost speed

# Numpy Arrays

## 1D, 2D are familiar
## 3D might look like stacks of 2D
## Numpy focuses on ND space as default - `ndarray`
## Data must be same type, size is static, shape cannot be jagged (e.g. no 2D array where dimensonality changes between elements within)

a = np.array([1, 2, 3])
a[2] = 5
a[1:] # 2, 5 -> Python's slice notation

b = a[1:] # Returns a "view" into an array, modifications affect original array

arrayWithThreePointsInFourDimensions = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [10,11,12,13]])

# Axis - dimensionality of an array... so arrayWithThreePointsInFourDimensions has 3 arrays with dimensionality 4 and arrayWithThreePointsInFourDimensions has 2 axis so a[1,3] # 8
# Axes - collection of axis

arrayWithThreePointsInFourDimensions[1,3] # 8

# Lots of NumPy functions work by specifying the axis...

sum = np.sum(arrayWithThreePointsInFourDimensions, axis = 1) # [10 26 46]
print(sum)


# rand takes n1...nN where n1...nN are dimensions (where all n exist in set of positive natural numbers)
np.random.rand(1) # array([0.2123])

np.random.rand(3) # array([0.1, 0.2, 0.3])

np.random.rand(3, 1) # array([[0.1], [0.6], [0.9]]

rand = np.random.rand(2, 1, 1) # array([ [ [ 0.1 ] ],
                               #         [ [ 0.9 ] ]])

dimensions = rand.ndim # 3
shape = rand.shape     # (2, 1, 1)
size = rand.size       # 2 (Count of flattened array)

# Can create arrays with np.zeros, np.ones, np.empty (make sure to fill)
# Can specify data types
# Arrays have sorting functions
# Can reshape 

# there's a bunch of other standard stuff in here we can look up later if we need it

# Broadcasting is pretty neat - can be used with same size arrays too

d = np.array([2, 4])
d * 2 # [4, 8]

# Awesome! We can leave this here for now. There's a bunch of further reading about matrices, but we get the gist
# and getting some practice reading the shapes of n dimensional arrays was pretty useful
