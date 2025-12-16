# Create a decorator to print the function name and the values of it's arguments every time the function is called
import time

def print_function_name(func):
    def wrapper(*args, **kwargs):
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{k}:{v}" for k, v in kwargs.items())

        print(f"Function name: {func.__name__}")
        print(f"{args_values}")
        print(f"{kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@print_function_name
def greet(name, msg):
    print(f"{name.capitalize()} says {msg}")

name = input("Enter name: ")
greet(name, msg = "Hello")