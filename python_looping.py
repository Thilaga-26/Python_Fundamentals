""" while loop """
i = 1
while i <= 10:
    print(i)
    i += 1
print("--------------------")

# print even no using while loop
print("Even No : ")
NUM = 20
i = 2
while i <= 20:
    print(i)
    i += 2
print("--------------------")

# Continue Statement
i = 1
while i <= 20:
    if i % 2 == 0:
        i = i + 1
        continue
    print(i)
    i += 1
print("--------------------")

# While Else
i=1
while i<=5:
    if i==4:
        break
    print(i)
    i+=1
else:
    print("Loop Completed")
print("--------------------")

# For Else
for i in range(1,21):
    if i==5:
        break
    print(i)
else:
    print("For Loop Completed")

print("--------------------")

# For Loop in Python
for i in range(0, 21, 2):
    print(i)

for i in range(5):
    var1=int(input("Enter a No : "))
    var2=int(input("Enter a No : "))
    print(var1+var2)
