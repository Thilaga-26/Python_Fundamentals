""" Python JSON """
import json

# Convert from JSON to Python
# some JSON:
VAR = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
var1 = json.loads(VAR)

# the result is a Python dictionary:
print(var1["age"])

# Convert from Python to JSON:
# a Python object (dict):
var = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
var1 = json.dumps(var)

# the result is a JSON string:
print(var1)

# Convert Python objects into JSON strings, and print the values:
# dict
print(json.dumps({"name": "John", "age": 30}))
# list
print(json.dumps(["apple", "bananas"]))
# tuple
print(json.dumps(("apple", "bananas")))
# string
print(json.dumps("hello"))
# int
print(json.dumps(42))
# float
print(json.dumps(31.76))
# True
print(json.dumps(True))
# False
print(json.dumps(False))
# None
print(json.dumps(None))

# Convert a Python object containing all the legal data types:
var = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(var, indent=4, sort_keys=True))
