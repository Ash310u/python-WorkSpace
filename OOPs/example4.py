# Encapsulation
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car():
    def __init__(self,__brand,model):
        self.model = model
        self.__brand = __brand

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

if __name__ == "__main__":
    print("Example 4: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.")
    print("-" * 50)
    my_car = Car("Toyota","Corolla")
    print("Brand by getter method: ",my_car.get_brand())
    my_car.set_brand("Ford")
    print("Brand after using setter method: ",my_car.get_brand())
    # print(my_car.__brand) # putting __ infront of the attribute makes it private and only accessible within the class
    # print(my_car.brand) # this will give an error because brand is not a attribute
    print("-" * 50)
    