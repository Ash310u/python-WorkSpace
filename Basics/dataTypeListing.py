x = [1, 2, 5, True, 0.45, 1, 'ab', 'cd', 'ef', False, 'False', 7]

type_count = {}

for item in x:
    # We use __name__ to get the name of the type as a string (e.g., 'int', 'str', 'bool').
    # If we just use type(item), it returns the type object itself (like <class 'int'>),
    # which is less readable and not as convenient for displaying or using as a dictionary key.
    t = type(item).__name__
    # This line updates the count of each data type found in the list 'x'.
    # It checks if the type name 't' is already a key in the 'type_count' dictionary.
    # If it is, it increments the count by 1; if not, it initializes the count to 1.
    type_count[t] = type_count.get(t, 0) + 1
    # Same Thing as above but using if else
    
    # if t in type_count:
    #     type_count[t] = type_count[t] + 1
    # else:
    #     type_count[t] = 1

for t, count in type_count.items():
    print(f"{t}: {count}")