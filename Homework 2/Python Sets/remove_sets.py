#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear the set completely by using the clear() method:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Delete the set completely by using the del keyword:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
