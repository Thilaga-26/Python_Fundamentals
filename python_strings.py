""" Assign String to a Variable """
str_var = input("Enter The String : ")
print(str_var)

# Strings are Arrays
print(str_var[1])

# Length of a String
print(len(str_var))

# Looping Through a String
for val in "banana":
    print(val)

# Check string
str_txt = input("Enter The String : ")
if "free" in str_txt:
    print("Yes, 'free' is present.")

# Check if NOT
str_txt = input("Enter The String : ")
if "expensive" not in str_txt:
    print("No, 'expensive' is NOT present.")

# Slicing
str_var = input("Enter The String : ")
print(str_var[2:5])
# Slice From the Start
print(str_var[:5])
# Slice To the End
print(str_var[2:])
# Negative Indexing
print(str_var[-5:-2])

# Modify Strings
str_var = input("Enter The String : ")
# Uppercase
print(str_var.upper())
# Lowercase
print(str_var.lower())
# Remove Whitespace
print(str_var.strip())
# Replace String
print(str_var.replace("H", "J"))
# Split String
print(str_var.split(","))

# String Concatenation
STR_VAR1 = "Hello"
STR_VAR2 = "World"
"""Concatenate the Strings"""
STRING = STR_VAR1 + " " + STR_VAR2
print(STRING)

# String Format
QUANTITY = 3
ITEM_NO = 567
PRICE = 49.95
MYORDER = "I want {} pieces of item {} for {} dollars."
print(MYORDER.format(QUANTITY, ITEM_NO, PRICE))

# Escape Characters
# Single Quote
MY_VAR = 'It\'s alright.'
print(MY_VAR)
# Backslash
MY_VAR = "This will insert one \\ (backslash)."
print(MY_VAR)
# New Line
MY_VAR = "Hello\nWorld!"
print(MY_VAR)
# Carriage Return
MY_VAR = "Hello\rWorld!"
print(MY_VAR)
# Tab
MY_VAR = "Hello\tWorld!"
print(MY_VAR)
# Backspace
MY_VAR = "Hello \bWorld!"
print(MY_VAR)
# Octal value
MY_VAR = "\110\145\154\154\157"
print(MY_VAR)
# Hex value
MY_VAR = "\x48\x65\x6c\x6c\x6f"
print(MY_VAR)
