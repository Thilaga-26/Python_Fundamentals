""" Local scope """
# A variable created inside a function is available inside that function:
def my_func():
    """
    This function print the variable as result.
    """
    int_var = 300
    print(int_var)

my_func()

# Function Inside Function
# The local variable can be accessed from a function within the function:
def my_outer_func():
    """
    This is Outer Function.
    """
    outer_var = 300
    def my_inner_func():
        """
        This is Inner Function.
        """
        print(outer_var)
        my_inner_func()

my_outer_func()


# Global Scope
# A variable created outside of a function is global and can be used by anyone:
MYVAR = 300

def myfunc():
    """
    This is Global scope Function.
    """
    print(MYVAR)

myfunc()

print(MYVAR)

# local and global scope
# global scope (outside the function)
VAR = 300

def myfunction():
    """
    This is Global scope Function.
    """
  # local scope(inside the function)
    var1 = 200
    print(var1)

myfunction()

print(VAR)
