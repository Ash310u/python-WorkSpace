# Polymorphism
# Demonstrate polymorphism by defining a mehtod fuel_type() in both Car and ElectricCar classes, but with different behavior.

from example2 import Car as CarBase
from example3 import ElectricCar as ElectricCarBase

class Car(CarBase):
    def fuel_type(self):
        return "Petrol or diesel"

class ElectricCar(ElectricCarBase):
    def fuel_type(self):
        return "Electric"

if __name__ == "__main__":
    print("Example 5: Demonstrate polymorphism by defining a mehtod fuel_type() in both Car and ElectricCar classes, but with different behavior.")
    print("-" * 50)

    my_car = Car("Toyota","Corolla")
    print(my_car.full_name())
    print("Fuel type: ",my_car.fuel_type())
    
    my_electric_car = ElectricCar("Tesla","Model S",100)
    print(my_electric_car.full_name())
    print("Fuel type: ",my_electric_car.fuel_type())
    
    print("-" * 50)