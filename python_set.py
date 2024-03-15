""" Create and print a Set """
set_var = {'Ram','Sam','Ravi'}
print(set_var)
# Specify a Variable Type
print(type(set_var))
# Access Values Using For loop
for var in set_var:
    print(var)
# Add - Adds an element to the set
set_var.add('Sara')
print(set_var)
# Update - Update the set with the union of this set and others
set_var1 = {'Kumar','Sundar','Suresh'}
set_var.update(set_var1)
print(set_var)
# Remove - Removes the specified element
set_var.remove('Sara')
print(set_var)
# Discard - Remove the specified item
set_var.discard('Suresh')
print(set_var)
# Pop - Removes an element from the set
set_var.pop()
print(set_var)
# Clear - Removes all the elements from the set
set_var.clear()
print(set_var)
# Delete a set_var
del set_var
# Set Methods
# Union - Return a set containing the union of sets
myVariable1 = {1, 2, 3, 4}
myVariable2 = {'a', 'b', 'c', 'd'}
myVariable = myVariable1.union(myVariable2)
print(myVariable)
# Union Update - Update the set with the union of this set and others
myVariable1.update(myVariable2)
print(myVariable1)
# Intersection - Returns a set, that is the intersection of two other sets
myVariable1 = {1, 2, 3, 4, 5}
myVariable2 = {5, 6, 7, 8, 9}
myVariable = myVariable1.intersection(myVariable2)
print(myVariable)
# intersection_update -
# Removes the items in this set that are not present in other, specified set(s)
myVariable1.intersection_update(myVariable2)
print(myVariable1)
# Symmetric_difference - Returns a set with the symmetric differences of two sets
myVariable=myVariable1.symmetric_difference(myVariable2)
print(myVariable)
# symmetric_difference_update - inserts the symmetric differences from this set and another
myVariable1.symmetric_difference_update(myVariable2)
print(myVariable1)
# isdisjoint - Returns whether two sets have a intersection or not
myVariable1 = {5,6,7}
myVariable2 = {5, 6, 7}
myVariable = myVariable1.isdisjoint(myVariable2)
print(myVariable)
# issubset - Returns whether another set contains this set or not
myVariable = myVariable1.issubset(myVariable2)
print(myVariable)
# issuperset - Returns whether this set contains another set or not
myVariable = myVariable1.issuperset(myVariable2)
print(myVariable)
