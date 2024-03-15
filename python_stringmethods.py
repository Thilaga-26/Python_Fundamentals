""" Assign String to a Variable """
str_var = input("Enter The String : ")
print(str_var)
# Specify a Variable Type
print(type(str_var))

# String Methods
# Converts a string into upper case
print(str_var.upper())
# Converts a string into lower case
print(str_var.lower())
# Converts the first character to upper case
print(str_var.capitalize())
# Converts the first character of each word to upper case
print(str_var.title())
# Converts the first character of each word to upper case
print(str_var.count("l"))
# Returns true if the string ends with the specified value
print(str_var.endswith("ld"))
# Searches the string for a specified value and returns the position of where it was found
print(str_var.find("o"))
# Searches the string for a specified value and returns the after position of where it was found
print(str_var.find("o", 5))
# Returns a string where a specified value is replaced with a specified value
print(str_var.replace("o", '0'))

# Assign String to a new Variable
STR_VAR1 = "thilo1234"
# Returns True if all characters in the string are upper case
print("Is Upper : ", STR_VAR1.isupper())
# Returns True if all characters in the string are lower case
print("Is Lower : ", STR_VAR1.islower())
# Returns True if all characters in the string are alphanumeric
print("Is Alpha Numeric : ", STR_VAR1.isalnum())
# Returns True if all characters in the string are in the alphabet
print("Is Alpha : ", STR_VAR1.isalpha())
# Splitlines
STR_VAR2 = "he\nis\ngood"
print(STR_VAR2)
print(STR_VAR2.splitlines())
print(STR_VAR2.splitlines(True))
# Split
# Splits the string at the specified separator, and returns a list
STR_VAR3 = "Python is a powerful language"
print(STR_VAR3.split(" "))
STR_VAR4 = "Python,is,a,powerful,language"
print(STR_VAR4.split(","))
# Strip
STR_VAR5="    thilo     "
# Returns the length of the String
print(len(STR_VAR5))
# Returns a trimmed version of the string
print(len(STR_VAR2.strip()))
# Returns a left trim version of the string
print(len(STR_VAR2.lstrip()))
# Returns a right trim version of the string
print(len(STR_VAR2.rstrip()))
# Partition
STR_VAR6='12-12-2020'
"""Returns a tuple where the string is parted into three parts"""
print(STR_VAR6.partition('-'))
