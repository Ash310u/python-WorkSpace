from numpy import *

arr = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

print(arr)

print("Shape of array:", arr.shape)
print("Size of array:", arr.size)
print("Dimension of array:", arr.ndim)

arr = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

print(arr)

print("Shape of array:", arr.shape)
print("Size of array:", arr.size)
print("Dimension of array:", arr.ndim)

# The number of dimensions is determined by how many arguments we pass to the reshape function, and the rightmost argument is the size of the deepest level of that array
print("Reshape of array: \n", arr.reshape(6,2)) # reshape(rows, columns) Basically any multiple of the size of the array
# 3d array
# print("3d Reshape of array: \n", arr.reshape(2,2,3)) # reshape(rows, columns, depth)
# 4d array
# print("4d Reshape of array: \n", arr.reshape(2,2,3,1)) # reshape(rows, columns, depth, depth)

print("Flatten of array:", arr.flatten()) # Flatten the array into a 1D array
print("Transpose of array: \n", arr.reshape(6,2).T) # Transpose the array
print("Sum of array:", arr.sum())

# Math Operations
print("Mean of array:", arr.mean()) # Mean of all elements in the array
print("Standard deviation of array:", arr.std()) # Standard deviation of all elements in the array