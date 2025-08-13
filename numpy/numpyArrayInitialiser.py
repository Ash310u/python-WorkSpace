import numpy as np

# 1. Using a Python list
a = np.array([1, 2, 3], dtype=float)
# a = np.array([1.0, 2.0, 3.0], int)
print("Array from list:", a)

# 2. Using a tuple
b = np.array((4, 5, 6))
print("Array from tuple:", b)

# 3. Using arange
# np.arange(start, stop, step) creates an array starting from 'start' up to (but not including) 'stop', with a step size of 'step'.
# Here, it creates an array: [0, 2, 4, 6, 8]
c = np.arange(0, 10, 2)
print("Array using arange:", c)

# 4. Using zeros
# np.zeros(shape) creates a new array of the given shape, filled with zeros.
# Here, it creates a 2x3 array (2 rows, 3 columns) of zeros.
d = np.zeros((2, 3))
print("Array of zeros:\n", d)

# 5. Using ones
# np.ones(shape) creates a new array of the given shape, filled with ones.
# Here, it creates an array of 5 ones.
e = np.ones(5)
print("Array of ones:", e)

# 6. Using linspace
# np.linspace(start, stop, num) creates an array of 'num' evenly spaced values between 'start' and 'stop'.
# Here, it creates an array: [0.0, 0.25, 0.5, 0.75, 1.0]
f = np.linspace(0, 1, 5)
print("Array using linspace:", f)

# 7. Using empty
# np.empty(shape) creates a new array of the given shape, without initializing the values.
# Note: This creates an array with random values. It's not really empty—it contains random memory values.
g = np.empty((2, 2))
print("Empty array:\n", g)

# 8. Using eye (identity matrix)
# np.eye(n) creates an identity matrix of size n x n, where the diagonal elements are 1 and the rest are 0.
# Here, it creates a 3x3 identity matrix.
h = np.eye(3)
print("Identity matrix:\n", h)

# 9. Using random
# np.random.rand(d0, d1, ..., dn) creates an array of the given shape, filled with random values between 0 and 1.
# Here, it creates a 2x2 array of random values.
i = np.random.rand(2, 2)
print("Random array:\n", i)