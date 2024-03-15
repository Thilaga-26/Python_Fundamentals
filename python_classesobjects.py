""" Create a Class"""
class Person:
    """
    A class representing an Person.
    """
    # The __init__() Function
    def __init__(self, name, age):
        """
        Initializes an MyClass object.
 
        Parameters:
            name (str): The name of the Person.
            age (int): The age of the Person.
        """
        self.name = name
        self.age = age

    def my_func(self):
        """
        Demonstrates triple double quotes
        to print the name.
        """
        print("Hello my name is " + self.name)

    # Modify Object Properties
    def myfunc(self):
        """
        Demonstrates triple double quotes
        to print the name.
        """
        print("Hello my name is " + self.name)

# Create Object
person1 = Person("John", 36)

print(person1.name)
print(person1.age)
person1.my_func()

person1.age = 40
print(person1.age)
