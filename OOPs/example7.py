# Static Methods
# Add a static method to the Car class that returns a general description of the car.

from example2 import Car as CarBase

class Car(CarBase):
    @staticmethod
    def get_description():
        return "This is a car with a brand and model"

if __name__ == "__main__":
    print("Example 7: Add a static method to the Car class that returns a general description of the car.")
    print("-" * 50)
    
    my_car = Car("Toyota","Corolla")
    # Although we're calling get_description() on the instance (my_car), it's still a static method.
    # Static methods can be called either on the class or an instance, but they do not receive the instance (self) as a parameter.
    print("Description by calling static method on instance: ", my_car.get_description())
    print("Description by static method: ",Car.get_description())
    
    print("-" * 50)