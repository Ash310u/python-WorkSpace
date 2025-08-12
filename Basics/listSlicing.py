# In Python, when you use [:] on a list, it creates a shallow copy of the list.
# For example:
lst1 = [1, 2, 3]
lst2 = lst1[:]  # This makes a new list with the same elements as lst1
# Difference between lst2 = lst1 and lst2 = lst1[:]
lst3 = lst1        # This does NOT create a new list; lst3 and lst1 refer to the same object
lst4 = list(lst1)  # This creates a shallow copy, like lst1[:]
lst5 = lst1.copy() # This also creates a shallow copy

print("lst3 (assigned):", lst3)
print("lst4 (list()):", lst4)
print("lst5 (copy()):", lst5)

# Demonstrate the difference
lst1.append(5)
print("After appending to lst1 again:")
print("lst1:", lst1)
print("lst3 (assigned, same object):", lst3)  # Will reflect the change
print("lst4 (list() copy):", lst4)            # Will NOT reflect the change
print("lst5 (copy()):", lst5)                 # Will NOT reflect the change
