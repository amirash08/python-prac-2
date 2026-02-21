#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Print each fruit in a fruit list, and its index:
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

#Use the break statement to stop the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Use the continue statement to skip the "banana" fruit:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Use the range() function to loop through a set of code a specified number of times:
for x in range(6):
    print(x)

# Use the else keyword to run a block of code once when the loop has finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#The pass statement is used when a statement is required syntactically, but you do not want any command or code to execute.
for x in [0, 1, 2]:
    pass

