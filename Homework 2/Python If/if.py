#If statement:
a = 33
b = 200
if b > a:
    print("b is greater than a")
#If...else statement:
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#One-line if statement:
a = 200
b = 33
print("A") if a > b else print("B")

#One-line if/else that prints a value:
a = 2
b = 330
print("A") if a > b else print("B")

#One line, three outcomes:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
