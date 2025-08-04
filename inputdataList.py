user_list = []

def take_user_details():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    user = {"roll": roll, "name": name, "address": address}
    user_list.append(user)

def print_user_details(user):
    print("Roll Number:", user["roll"])
    print("Name:", user["name"])
    print("Address:", user["address"])

num_students = int(input("How many students to add? "))

for _ in range(num_students):
    take_user_details()

print("--------------------------------")
print("Stored user data:")
for user in user_list:
    print_user_details(user)
    print("----------------")
