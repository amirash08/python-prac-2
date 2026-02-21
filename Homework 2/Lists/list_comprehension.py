fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#With no if statement:
newlist = [x for x in fruits]
print(newlist)

#Range to create a list containing the number 1 to 10:
newlist = [x for x in range(10)]
print(newlist)

#only lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
