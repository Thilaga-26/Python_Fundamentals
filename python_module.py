""" Import the module named mymodule """
import platform
import mymodule

# Call the greeting function:
mymodule.greeting("Jonathan")

# Import the module named mymodule, and access the person1 dictionary:
my_var = mymodule.person1["age"]
print(my_var)

# Built-in Modules
# platform module

my_var = platform.system()
print(my_var)

# Using the dir() Function
directory = dir(platform)
print(directory)
