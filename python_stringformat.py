""" Add a placeholder where you want to display the price """
COST = 49
TXT = "The cost is {} dollars"
print(TXT.format(COST))

# Add more placeholders
QUANTITY = 3
ITEMNO = 567
PRICE = 49
MYORDER = "I want {} pieces of item number {} for {:.2f} dollars."
print(MYORDER.format(QUANTITY, ITEMNO, PRICE))

# Index Numbers
QUANTITY = 3
ITEMNO = 567
PRICE = 49
MYORDER = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(MYORDER.format(QUANTITY, ITEMNO, PRICE))

# Want to refer to the same value more than once, use the index number
AGE = 36
NAME = "John"
TXT = "His name is {1}. {1} is {0} years old."
print(TXT.format(AGE, NAME))

# Named Indexes
MYORDER = "I have a {carname}, it is a {model}."
print(MYORDER.format(carname = "Ford", model = "Mustang"))
