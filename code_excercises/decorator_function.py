def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

def my_function():
    print("This is the original function.")

my_function = my_decorator(my_function)
if __name__ == "__main__":
    my_function()