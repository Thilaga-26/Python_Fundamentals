""" Built-in Data Types """
# Getting input as String value from user
my_var = input("Enter The String : ")
print(my_var)
# Specify a Variable Type
print(type(my_var))
# Getting input as Integer values from user
var_one = int(input("Enter The Value of var_one : "))
var_two = int(input("Enter The Value of var_two : "))
"""Add two numbers"""
print(var_one + var_two)
# Getting input as Float values from user
var_one = float(input("Enter The Value of var_one : "))
var_two = float(input("Enter The Value of var_two : "))
"""Sub two numbers"""
print(var_one - var_two)

# Getting input as complex numbers
VAR_ONE = 3+5j
VAR_TWO = 5j
VAR_THREE = -5j
"""Add and Sub three complex numbers"""
print(VAR_ONE + VAR_TWO - VAR_THREE)

# Getting input as list
listVariables = ["apple", "banana", "cherry"]
"""Iterate list through loop"""
for my_var in listVariables:
    print(my_var)

# Getting input as tuple
tupleVariables = ("Ram", "Ragu", "Ravi")
"""Iterate tuple through loop""" 
for my_var in tupleVariables:
    print(my_var)

# Getting range inputs
f = range(6)
print(f)

# Getting input as dictionary
dictVariables = {"myName" : "John", "myAge" : 36}
"""Iterate dictionary through loop""" 
for var_one, var_two in dictVariables.items():
    print(var_one, var_two)

# Getting input as set
setVariables = {"White", "Red", "Yellow"}
"""Iterate set through loop"""  
for my_var in setVariables:
    print(my_var)

# Getting input as frozenset
myFrozenset = ['apple', 'banana', 'cherry']
var = frozenset(myFrozenset)
print(var)

# Getting input as bool
NUM1 = 10
NUM2 = 5
# Checking the bool condition whether it is trur or false
print(NUM1>NUM2)

# Binary Types(memoryview, bytearray, bytes)
# Getting input as byte
VAR = b"Hello"
print(VAR)

# Getting input as bytearray
var = bytearray(5)
print(var)

# Getting input as memoryview
variable = memoryview(bytes(5))
print(variable)
