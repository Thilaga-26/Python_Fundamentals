""" Create and print a Tuple """
# tuples allows multiple datatypes
tup_var = (1, 2.5, True, "Ram")
print(tup_var)
# Specify a Variable Type
print(type(tup_var))
# Access Tuple Items
print(tup_var[1])
# negative indexing
print(tup_var[-1])
# Silicing
print(tup_var[0:2])
# Typecast tuple to list
list_var = list(tup_var)
print(list_var)
# append - Adds an element at the end of the list
list_var.append("Raja")
print(list_var)
# Specify a Variable Type
print(type(list_var))
# Typecast list to tuple
tup_var = tuple(list_var)
print(tup_var)
# Specify a Variable Type
print(type(tup_var))
# Tuples through Looping
for val in tup_var:
    print(val)
# If statement
if "Raj" in tup_var:
    print("Raja is Found")
else:
    print("Not Found")
# Length of the tuple
print(len(tup_var))
# Creating a Tuple
tup = (1,)
# Specify a Variable Type
print(type(tup))
# delete tuple
del tup
# Create a Tuples
tup_var1 = (1, 2, 7, 4)
tup_var2 = (5, 6, 7, 8)
# Concatenate a tuples
tup_variable = tup_var1 + tup_var2
print(tup_variable)
print(tup_variable.count(7))
# Use Separater to connect a tuples
tup_variable = (tup_var1, tup_var2)
print(tup_variable)
# Access Items using indexing
print(tup_variable[0])
print(tup_variable[1])
print(tup_variable[0][1])
# Return a min & max values in tuples
print(min(tup_var1))
print(max(tup_var1))
