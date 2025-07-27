user_input = input("Enter a number: ")

num = float(user_input)
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("Invalid input. Please enter a numeric value.")


marks = float(input("Enter your marks: "))
if marks > 100:
    print("Outstanding")
else:
    if marks >= 30:
        print("Good")
    else:
        print("Failed")
