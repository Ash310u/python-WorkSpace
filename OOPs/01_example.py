# Create a car class with attributes like brand and model.Then create an instance of this class

class Car:
    # __init__ is the constructor method of the class
    def __init__(self, brand, model): # Self is the instance of the class
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.__dict__)

my_new_car = Car("Ford", "Mustang")
print(my_new_car.__dict__)