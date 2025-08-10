student = []

def takeStudentDetails(roll, name, address = "Not provided"):
    student.append({name, roll, address})
    return 

name = input("Enter name: ")
roll = input("Enter roll: ")
address = input("Enter address: ")

takeStudentDetails(name, roll, address)

print(student[0])