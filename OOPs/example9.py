# Class Inheritance and isinstance() Function
# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

from example5 import Car as CarBase
from example5 import ElectricCar as ElectricCarBase

if __name__ == "__main__":
    print("Example 9: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.")
    print("-" * 50)

    my_tesla = ElectricCarBase("Tesla","Model S",100)
    print(isinstance(my_tesla,CarBase))
    print(isinstance(my_tesla,ElectricCarBase))

    print("-" * 50)