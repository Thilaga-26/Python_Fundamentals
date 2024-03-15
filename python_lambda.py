""" Add 50 to argument var, and return the result """
def txt_var(var): return var + 50
print(txt_var(5))

# Lambda functions
def myfunc(num):
    """This function Multiply two numbers and print the result."""
    return lambda var : var * num

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
