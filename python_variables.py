""" Legal variable name """
MY_VAR = "Python"

# Many Values to Multiple Variables
var_one, var_two, var_three = "is ", "a ", "high-level programming language"

# One Value to Multiple Variables
MYVAR_ONE = MYVAR_TWO = MYVAR_THREE = "popularly used for website development."

# Output Variable
print(MY_VAR, MYVAR_ONE, MYVAR_TWO, MYVAR_THREE, MYVAR_ONE)


# A simple Python function to demonstrate global variable m inside the function
def my_func():
    """
    This function get the data from global variable m and print the result.
    """
    m = "powerful programming language"
    print("Python is a  " + m)

# Driver code to call a function
my_func()
