# Add a method to the Car class that displays the full name of the car(brand and model)
from example1 import Car as CarBase
class Car(CarBase):
    def full_name(self):
        return f"{self.brand}-{self.model}"

if __name__ == "__main__":
    print("Example 2: Add a method to the Car class that displays the full name of the car(brand and model)")
    print("-" * 50)
    
    my_car = Car("Toyota","Corolla")
    print(my_car.full_name())
    
    print("-" * 50)