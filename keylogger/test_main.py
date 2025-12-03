# my_module.py

def greet(name):
    print(f"Hello, {name}!")

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

if __name__ == '__main__':
    # This code will only run when my_module.py is executed directly
    print("Running directly as main script.")
    greet("World")

    #print(message)

    obj = MyClass(10)
    obj.display()