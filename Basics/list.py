my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("Elements from index 1 to 3:", my_list[1:4])

print("Max value:", max(my_list))
print("Min value:", min(my_list))
print("Sum of elements:", sum(my_list))

print("Count of 2 in my_list:", my_list.count(2))
print("Index of 4 in my_list:", my_list.index(4))

my_list.append(6)
print("List after appending 6:", my_list)

my_list.insert(0, 0)
print("List after inserting 0 at index 0:", my_list)

del my_list[2]
print("List after deleting element at index 2:", my_list)

my_list.clear()
print("Cleared list:", my_list)

my_list = [1, 2, 3, 4, 5]
a, b, c, d, e = my_list
print("Unpacked values:", a, b, c, d, e)

print("Length of my_list:", len(my_list))

for item in my_list:
    print("Item:", item)

nested_list = [1, [2, 3], [4, 5]]
print("Nested list:", nested_list)
print("Accessing nested element:", nested_list[1][0])
