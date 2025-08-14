import numpy as np

# Example array
arr = np.array([1, np.e, 10, 100])

# Concatenate two arrays
arr2 = np.array([1000, 10000])
concatenated = np.concatenate((arr, arr2))
print("Concatenated array:", concatenated)

# Square root of array elements
sqrt_arr = np.sqrt(arr)
print("Square root of arr:", sqrt_arr)

# Array copying using view (shallow copy)
# A shallow copy of a numpy array (using .view()) creates a new array object that looks at the same data as the original array.
# This means changes to the data in one array will be reflected in the other, but changes to the shape (like resizing) will not affect the other.
arr_view = arr.view()
print("View of arr:", arr_view)

# Array copying using copy (deep copy)
# A deep copy of a numpy array (using .copy()) creates a new array object with a new memory location for the data.
# This means changes to the data in one array will not affect the other, and changes to the shape (like resizing) will not affect the other.
arr_copy = arr.copy()
print("Copy of arr:", arr_copy)

# Logarithmic functions
print("Natural log (ln) of arr:", np.log(arr))
print("Base-10 log of arr:", np.log10(arr))
print("Base-2 log of arr:", np.log2(arr))

# Trigonometric functions
angles = np.array([0, np.pi/6, np.pi/4, np.pi/2, np.pi])
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
values = np.array([0, 0.5, 1])
print("arcsin of values:", np.arcsin(values))
print("arccos of values:", np.arccos(values))
print("arctan of values:", np.arctan(values))