states_data = [
    [10, 20, 30, 40],
    [15, 25, 35],
    [5, 10, 15, 20, 25],
    [100, 200],
    [1, 2, 3, 4, 5, 6]
]

print("=" * 70)
print("STATE LIST ANALYSIS PROGRAM")
print("=" * 70)
print()

print("Original State List:")
print(states_data)
print()

total_sum = sum(sum(sublist) for sublist in states_data)
print(f"Total sum of all elements: {total_sum}")


# Initialize max_element to negative infinity so any number in the lists will be larger
max_element = float('-inf')
max_index = -1

for i, sublist in enumerate(states_data):
    if sublist:  # Check if sublist is not empty
        current_max = max(sublist)
        if current_max > max_element:
            max_element = current_max
            max_index = i

print(f"Maximum element in the entire list: {max_element}")
print(f"Index of list containing maximum element: {max_index}")

# Count total number of elements
total_elements = sum(len(sublist) for sublist in states_data)
print(f"Total number of elements: {total_elements}")

# Print each sublist with its index and sum
print("\nDetailed breakdown:")
for i, sublist in enumerate(states_data):
    sublist_sum = sum(sublist) if sublist else 0
    print(f"List {i}: {sublist} (Sum: {sublist_sum})")

print("\n" + "=" * 70)
print("You can modify the states_data list above to test with different data")
print("\n" + "=" * 70)
