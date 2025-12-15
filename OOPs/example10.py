# Multiple Inheritance
# Create two classes Battery and Engine, and let ElectricCar class inherit from both, demonstrating multiple inheritance.

from example3 import ElectricCar as ElectricCarBase

class Battery:
    def battery_type(self):
        return "Lithium-ion"

class Engine:
    # The 'pass' statement is a placeholder that does nothing; it's used when a statement is syntactically required but you don't want to execute any code.
    pass

class ElectricCar(ElectricCarBase,Battery,Engine):
    pass

if __name__ == "__main__":
    print("Example 10: Create two classes Battery and Engine, and let ElectricCar class inherit from both, demonstrating multiple inheritance.")
    print("-" * 50)

    my_tesla = ElectricCar("Tesla","Model S",100)
    print(my_tesla.full_name())
    print("Battery type: ",my_tesla.battery_type())
    
    print("-" * 50)