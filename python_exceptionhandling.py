""" Try Except """
# Try block will generate an exception, because x is not defined:
try:
    print(var)
except:
    print("An exception occurred")

# Many Exceptions
# Print one message if the try block raises a NameError and another for other errors
try:
    print(var)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
# try block does not generate any error:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
try:
    print(var)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Raise an exception
VAR = -1
if VAR < 0:
    raise Exception("Sorry, no numbers below zero")
