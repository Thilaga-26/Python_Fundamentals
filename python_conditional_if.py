""" IF Else Statement in Python """
name_var = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
# The conditions is true, then print Eligible for vote.
if age >= 18:
    print(name_var, " age is ", age, " Eligible for Vote.")
#Else print Not Eligible for Vote
else:
    print(name_var, " age is ", age, " Not Eligible for Vote.")

# elif Statement in Python
days = int(input("Enter The Days : "))
# The conditions is true, then print Good No Fine.
if days == 0:
    print("Good No Fine")
# The conditions is between 1 & 5, then print days*Fine Amount.
elif 1 <= days <= 5:
    print("Fine Amount : ", days * 0.5)
# The conditions is between 5 & 10, then print days*Fine Amount.
elif 5 <= days <= 10:
    print("Fine Amount : ", days * 1)
# The conditions is between 10 & 30, then print days*Fine Amount.
elif 10 <= days <= 30:
    print("Fine Amount : ", days * 5)
# Else, then print Membership Cancel.
else:
    print("Membership Cancel")

# Nested If Statement in Python
var_one = int(input("Enter Mark-1  : "))
var_two = int(input("Enter Mark-2  : "))
var_three = int(input("Enter Mark-3  : "))
"""Add three numbers"""
total = var_one + var_two + var_three
"""Calculate average"""
average = total / 3.0
print("Total  : ", total)
print("Average  : ", average)
# If Statement
# result is pass then enter into this condition.
if var_one >= 35 and var_two >= 35 and var_three >= 35:
    print("Result  : Pass")
    # Nested if Statement
    # The conditions is between 90 & 100, then print A.
    if 90 <= average <= 100:
        print("Grade : A")
    # The conditions is between 80 & 89, then print B.
    elif 80 <= average <= 89:
        print("Grade : B")
    # The conditions is between 70 & 79, then print C.
    elif 70 <= average <= 79:
        print("Grade : C")
    # Else print Grade D.
    else:
        print("Grade : D")
# Else , print Fail and No Grade.
else:
    print("Result  : Fail")
    print("Grade   : No Grade")
