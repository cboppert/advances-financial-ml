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
