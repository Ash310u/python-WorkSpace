# Create an ElectricCar class that inherits from the Car class has additional attributes

from example2 import Car as CarBase

class ElectricCar(CarBase):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


if __name__ == "__main__":
    print("Example 3: Create an ElectricCar class that inherits from the Car class has additional attributes")
    print("-" * 50)
    
    my_electric_car = ElectricCar("Tesla","Model S",100)
    print(my_electric_car.full_name())
    
    print("-" * 50)