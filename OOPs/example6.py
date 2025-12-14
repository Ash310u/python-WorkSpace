# Class Variables
# Add a class variable to Car that keeps track of the number of cars created.

from example2 import Car as CarBase

class Car(CarBase):
    car_count = 0
    def __init__(self,brand,model):
        super().__init__(brand,model)
        Car.car_count += 1
    
    def get_car_count(self):
        return Car.car_count

if __name__ == "__main__":
    print("Example 6: Add a class variable to Car that keeps track of the number of cars created.")
    print("-" * 50)

    my_car = Car("Toyota","Corolla")
    print(my_car.brand)
    my_new_car = Car("Ford","Mustang")
    print(my_new_car.full_name())
    my_third_car = Car("Chevrolet","Camaro")
    print(my_third_car.full_name())
    my_fourth_car = Car("BMW","M3")
    print(my_fourth_car.full_name())
    my_fifth_car = Car("Mercedes","C-Class")
    print(my_fifth_car.full_name())
    
    print("-" * 50)
    
    print("Number of cars created: ",my_fifth_car.get_car_count())
    
    print("-" * 50)