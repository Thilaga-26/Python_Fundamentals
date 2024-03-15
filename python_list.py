""" Create and print a List """
my_list = [1, 2, 3, 4, 5]
print(my_list)
# Specify a Variable Type
print(type(my_list))

# Access List Items
my_list[0] = 100
print(my_list)

# Slicing in list
print(my_list[1])
# Negative Indexing
print(my_list[-1])
# Slice From the Start
print(my_list[:3])
# Slice To the End
print(my_list[2:])
print("-----------")

# List allows Multiple datatypes
listVariables = [1, True, 'Ram', 2.5, [1, 2, 3, 4]]
print(listVariables)
# Specify a Variable Type
print(type(listVariables))
print(listVariables[0], " type is ", type(listVariables[0]))
print(listVariables[1], " type is ", type(listVariables[1]))
print(listVariables[2], " type is ", type(listVariables[2]))
print(listVariables[3], " type is ", type(listVariables[3]))
print(listVariables[4], " type is ", type(listVariables[4]))
print(listVariables[4][1])
print("-----------")

# List Methods
myVar = [10, 25, 35, 45]
print(myVar)
# Removes all the elements from the list
myVar.clear()
print(myVar)
myVar = [10, 25, 35, 45]
# Returns a copy of the list
myVar1 = myVar.copy()
print(myVar1)
myVar2 = [10, 25, 35, 45, 25, 4, 25]
# Returns the number of elements with the specified value
print(myVar2.count(25))
# Returns the index of the first element with the specified value
print(myVar2.index(25))
# Returns the length of the list
print(len(myVar2))
# Returns the Maximum value in list
print(max(myVar2))
# Returns the Minimum value in list
print(min(myVar2))
# remove Element using index
myVar2.pop(0)
print(myVar2)

my_var = [10, 25, 35, 45, 25, 4, 25]
# remove Values in list
my_var.remove(25)
print(my_var)
print("-----------")

# create a list1
nameList = ["Ram"]
print(nameList)
# append - Adds an element at the end of the list
nameList.append("Sam")
nameList.append("Ravi")
nameList.append("Kumar")
print(nameList)
# create a list2
nameList2 = ["Sara", "Anitha"]
# extend - Add the elements of a list (or any iterable), to the end of the current list
nameList.extend(nameList)
print(nameList)
# insert - Adds an element at the specified position
nameList.insert(0,"Suriya")
print(nameList)
print("-----------")

listVar = [10,50,100,25,85]
print(listVar)
# sort - Sorts the list
listVar.sort()
print(listVar)
# reverse - Reverses the order of the list
listVar.sort(reverse=True)
print(listVar)

listStr=["Orange","Apple","Zebra"]
# sort - Sorts the list
listStr.sort()
print(listStr)
# reverse - Reverses the order of the list
listStr.sort(reverse=True)
print(listStr)
# Sort using key length
listStr.sort(key=len)
print(listStr)
