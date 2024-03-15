""" Arithmetic Operators """
num1 = int(input("Enter The Value of num1 : "))
num2 = int(input("Enter The Value of num2 : "))
# Addition
print(num1 + num2)
# Subtraction
print(num1 - num2)
# Multiplication
print(num1 * num2)
# Division
print(num1 / num2)
# Modulus
print(num1 % num2)
# Exponentiation
print(num1 ** num2)
# Floor division
print(num1 // num2)

# Assignment Operators
num = int(input("Enter The Value of num : "))
print(num)
num += 3
print(num)
num -= 3
print(num1)
num *= 3
print(num)
num /= 3
print(num)
num %= 3
print(num)
num //= 3
print(num)
num **= 3

# Comparison Operators
num1 = int(input("Enter The Value of num1 : "))
num2 = int(input("Enter The Value of num2 : "))
# Equal
print(num1 == num2)
# Not equal
print(num1 != num2)
# Greater than
print(num1 > num2)
# Less than
print(num1 < num2)
# Greater than or equal to
print(num1 >= num2)
# Less than or equal to
print(num1 <= num2)

# Logical Operators
num = int(input("Enter The Value of num : "))
# Returns True if both statements are true
print(3 < num < 10)
# Returns True if one of the statements is true
print(num > 3 or num < 4)
# Reverse the result, returns False if the result is true
MY_VAR = not 3 < num < 10
print(MY_VAR)

# Identity Operators
myVar1 = ["apple", "banana"]
myVar2 = ["apple", "banana"]
myVar = myVar1
# is - Returns True if both variables are the same object
print(myVar1 is myVar)
print(myVar1 is myVar2)
print(myVar1 == myVar2)
# is not - Returns True if both variables are the same object
print(myVar1 is not myVar)
print(myVar1 is not myVar2)
print(myVar1 != myVar2)

# Membership Operators
myVar = ["apple", "banana"]
# in - Returns True if a sequence with the specified value is present in the object
print("banana" in myVar)
# not in - Returns True if a sequence with the specified value is not present in the object
print("banana" not in myVar)

# Bitwise Operators
num1 = int(input("Enter The Value of num1 : "))
num2 = int(input("Enter The Value of num2 : "))
# AND - Sets each bit to 1 if both bits are 1
print(num1 & num2)
# OR	- Sets each bit to 1 if one of two bits is 1
print(num1 | num2)
# XOR - Sets each bit to 1 if only one of two bits is 1
print(num1 ^ num2)
# NOT - Inverts all the bits
print(~num1)
# Zero fill left shift - Shift left by pushing zeros in from the right and
# let the leftmost bits fall off
print(num1 << num2)
# Signed right shift - Shift right by pushing copies of the leftmost bit in from the left,
# and let the rightmost bits fall off
print(num1 >> num2)
