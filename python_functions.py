""" A simple Python function """
def welcome_function():
    """
    Demonstrates triple double quotes
    Welcome and does nothing really.
    """
    print("Welcome ... ")

# Driver code to call a function
welcome_function()

# No Return Type Without Argument Function in Python
def add_function():
    """
    This function Adds two numbers and print the result.
    """
    var_one = int(input("Enter The Value of var_one : "))
    var_two = int(input("Enter The Value of var_two : "))
    my_var = var_one + var_two
    print("Total ",my_var)

# Driver code to call a function
add_function()

# No Return Type With Argument Function in Python
def sub_function(var_one,
                var_two):
    """
    Subtracts two numbers and print the result.
     
    Args:
        var_one (int): The first number.
        var_two (int): The second number.
    """
    my_var = var_one - var_two
    print("Difference : ", my_var)

# Driver code to call a function
sub_function(25, 2)

# Return Type Without Argument Function in Python
def mul_function():
    """
    Multiplies two numbers and returns the result.
    """
    var_one = int(input("Enter The Value of var_one : "))
    var_two = int(input("Enter The Value of var_two : "))
    my_var = var_one * var_two
    return my_var

# Driver code to call a function
myReturnVariable = mul_function()
print("Mul : ",myReturnVariable)

# Return Type With Argument Function in Python
def div_function(var_one, var_two):
    """
    Divide two numbers.
 
    Arguments
    ----------
    var_one : int
        The dividend.
    var_two : int
        The divisor.
 
    Returns
    -------
    int : The quotient of the division.
    """
    my_var = var_one / var_two
    return my_var

# Driver code to call a function
MYRETURNVARIABLE = div_function(25, 2)
print("Division : ", MYRETURNVARIABLE)

# Arbitrary Arguments Function in Python (*)
# A simple Python function to illustrate
# *studentsBio for variable number of arguments
def school_details(*studentsBio):
    """
    Using Arbitrary Arguments , providing list of data arguments and print the result
     
    Args:
        studentsBio (tuple): Variable number of arguments.
    """
    print(studentsBio)
    for user in studentsBio:
        print(user)

#Assigning values
school_details("Ram", "Sam", "Raja", "Sara")

# Keyword Arguments Function in Python
# A simple Python function to demonstrate Keyword Arguments
def message_function(my_name, my_age):
    """
    Using Keyword Arguments , 
    assigning the values for keys we can change the key orders 
    and print the result
     
    Args:
        my_name (String): String arguments.
        my_age (int):  age .
    """
    print(my_name, " age is ", my_age)

# Keyword arguments
message_function(my_age=25, my_name="Ram")

# Arbitrary Keyword Arguments in Python(**)
# A simple Python function to demonstrate
# *data for variable number of keyword arguments
def bio_data_student(**bio_data):
    """
    Using Arbitrary Keyword Arguments , 
    providing Key and Value datas and print the result
     
    Args:
        bio_data (Dictionary): variable number of key value arguments.
    """
    print(bio_data)

# Driver code
bio_data_student(myName="Ram Kumar", myAge=25, myGender="Male")

# Default Parameter Function in Python
# A simple Python function to demonstrate
# default arguments
def user_function(my_name, var_city="Salem"):
    """
    Using Default Parameter Function Arguments , 
    Not providing data for arguments its automatically takes the values from arguments 
    and print the result
     
    Args:
        my_name (String): String arguments.
        var_city (String): String arguments.
    """
    print(my_name, " is from ", var_city)

# Driver code (We call user_function() with only
# argument)
user_function("Ram", "Namakkal")
user_function("Sam")

# Passing a List as an Argument in Function Python
def total_function(var_marks):
    """
    In this function, providing list of data arguments and return the result
     
    Args:
        var_marks (int): Integer numbers.

    Returns:
        list : sum of Marks.    
    """

    return sum(var_marks)

# Print the total Marks
print("Total : ",total_function([55, 75, 80, 95, 47]))

# recursive function
def factorial(my_var):
    """
    This function provides Factorial of given number and return the result. 

    Args:
        my_var (int): Integer numbers.

    Returns:
        int : returns the factorial of given number.    
    """
    # Using if-else statement
    if my_var == 1:
        return 1
    return my_var * factorial(my_var - 1)

# Driver code to call a function
print("Factorial : ", factorial(5))
