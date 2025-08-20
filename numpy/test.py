from numpy import *

arr = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

# Matrix Operations
m1 = matrix(arr.reshape(4,3))
m2 = matrix('1 2 3; 4 5 6; 7 8 9; 10 11 12')

# Arithmetic Operations
print("Matrix addition: \n", m1 + m2)
print("Matrix subtraction: \n", m1 - m2)
print("Matrix multiplication: \n", m1 * arr.reshape(3,4))
print("Matrix division: \n", m1 / m2)
print("Matrix absolute: \n", abs(m1))x

# Matrix Properties
print("Matrix min: \n", m1.min())
print("Matrix max: \n", m1.max())
print("Matrix inverse: \n", m1.I)
print("Matrix transpose: \n", m1.T)
print("Matrix trace: \n", m1.trace())
print("Matrix diagonal: \n", m1.diagonal())
print("Matrix shape: \n", m1.shape)
print("Matrix size: \n", m1.size)
print("Matrix ndim: \n", m1.ndim)
# The itemsize attribute returns the size (in bytes) of each element in the matrix.
print("Matrix itemsize: \n", m1.itemsize)
# The nbytes attribute returns the total size (in bytes) of the matrix.
print("Matrix nbytes: \n", m1.nbytes)

# matrix Multiplication
m3 = matrix('1 2 3; 4 5 6; 7 8 9')
m4 = matrix('1 2 3; 4 5 6; 7 8 9')
print("Matrix multiplication: \n", m3 * m4)
print("Matrix multiplication: \n", m3 * arr.reshape(3,4))
print("Matrix multiplication: \n", m4 * arr.reshape(3,4))