# Property Decorators
# Use a property decorators in the Car class to make the model attribute read-only.

class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
    
    def full_name(self):
        return f"{self.brand}-{self.__model}"

    @property
    def model(self):
        return self.__model


if __name__ == "__main__":
    print("Example 8: Use a property decorators in the Car class to make the model attribute read-only.")
    print("-" * 50)
    
    my_car = Car("Toyota","Corolla")
    print("Full name: ",my_car.full_name())
    print("Model: ",my_car.model)
    
    print("Model after setting model: ",my_car.model)
    
    print("-" * 50)