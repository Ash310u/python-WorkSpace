# This method is called "shallow copying" when you append the same list object multiple times,
# causing all rows to reference the same list. This leads to unexpected behavior when modifying elements.

matrix = []
row = [0] * 3
for i in range(3):
    matrix.append(row)  # Shallow copy: all rows are the same object

matrix[0][0] = 99  # This changes the [0][0] of every row, since they're the same object
print(matrix)  # Output: [[99, 0, 0], [99, 0, 0], [99, 0, 0]]

# To avoid this, use "deep copying" or create a new list for each row:
matrix_fixed = []
for i in range(3):
    matrix_fixed.append([0] * 3)  # Deep copy: new list each time

matrix_fixed[0][0] = 99
print(matrix_fixed)  # Output: [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
