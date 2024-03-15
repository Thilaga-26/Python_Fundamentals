""" Create an Arrays containing car names """
cars=["Ford" , "Volvo" , "BMW"]
print(cars)
print("-----------------------------")

# Get the value of the first array item
MY_VAR = cars[0]
print(MY_VAR)
print("-----------------------------")

# Modify the value of the first array item
cars[0] = "Toyota"
print(cars)
print("-----------------------------")

# The Length of an Array
MY_VAR = len(cars)
print(MY_VAR)
print("-----------------------------")

# Looping Array Elements
for var in cars:
    print(var)
print("-----------------------------")

# Adding Array Elements
cars.append("Honda")
for var in cars:
    print(var)
print("-----------------------------")

# Delete the second element of the cars array
cars.pop(1)
for var in cars:
    print(var)
print("-----------------------------")

# Delete the element that has the value Honda
cars.remove("Honda")
for var in cars:
    print(var)
print("-----------------------------")

# Sort the element
cars.sort()
for var in cars:
    print(var)
print("-----------------------------")

#clear the element
cars.clear()
for var in cars:
    print(var)
print("-----------------------------")
