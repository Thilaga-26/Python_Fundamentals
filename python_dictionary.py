""" Create and print a dictionary """
userVar = {
    "name": "Ram",
    "age": 25,
    "isMarried": True
}
print(userVar)
# Specify a Variable Type
print(type(userVar))
# Access Dictionary Items
print(userVar["name"])
print(userVar.get('age'))
print(userVar.keys())
print(userVar.values())
print(userVar.items())
# Dictionary Values through Looping
# values - Returns a list of all the values in the dictionary
for x in userVar.values():
    print(x)
# keys - Returns a list containing the dictionary's keys
for x in userVar:
    print(x)
# items - Returns a list containing a tuple for each key value pair
for x,y in userVar.items():
    print(x,y)
# If Statement
if "gender" in userVar:
    print("Present")
else:
    print("No")
# update - Updates the dictionary with the specified key-value pairs
userVar.update({"gender":"male"})
print(userVar)
userVar["age"]=35
print(userVar)
# pop - Removes the element with the specified key
userVar.pop("age")
print(userVar)
# Clear - Removes all the elements from the Dictionary
userVar.clear()
print(userVar)
# Inside Dictionaries
users_var={
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True
    },
"user2": {
        "name": "Sam",
        "age": 35,
        "isMarried": False
    }
}
print(users_var)
