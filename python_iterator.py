""" Iterator vs Iterable """
# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:
MYSTR = "banana"
myit = iter(MYSTR)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

# Looping Through an Iterator
# Iterate the values of a tuple:
for var in mytuple:
    print(var)

# Iterate the characters of a string:
MYSTR = "banana"

for var in MYSTR:
    print(var)
