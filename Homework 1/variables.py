def ex1():
    x = 5
    y = "John"
    print(x)
    print(y)
    a = 4       # a is of type int
    a = "Sally" # a is now of type str
    print(a)
    b = str(3)    # b will be '3'
    c = int(3)    # c will be 3
    d = float(3)  # d will be 3.0
    x = 5
    y = "John"
    print(type(x))
    print(type(y))
    x = "John"
    # is the same as
    x = 'John'
    a = 4
    A = "Sally"
    #A will not overwrite a
def ex2(): 
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    #Camel Case 
    myVariableName = "John"
    #Pasal Case
    MyVariableName = "John"
    #Snake Case 
    my_variable_name = "John"
def ex3(): 
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)
    a = b = c = "Orange"
    print(a)
    print(b)
    print(c)
    fruits = ["apple", "banana", "cherry"]
    e, f, g = fruits
    print(e)
    print(f)
    print(g)
def ex4():
    x = "Python"
    y = "is"
    z = "awesome"
    print(x, y, z)
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)
    x = 5
    y = 10
    print(x + y)
    x = 5
    y = "John"
    print(x, y)
def ex5():
    x = "awesome"

    def myfunc():
        print("Python is " + x)

    myfunc()
    x = "awesome"

    def myfunc():
        x = "fantastic"
        print("Python is " + x)

    myfunc()

    print("Python is " + x)
    def myfunc():
        global x
        x = "fantastic"

    myfunc()

    print("Python is " + x)
    x = "awesome"

    def myfunc():
        global x
        x = "fantastic"

    myfunc()

    print("Python is " + x)
choice = int(input("1 or 2 or 3 or 4 or 5: "))
if choice == 1:
    ex1()
if choice == 2:
    ex2()
if choice == 3: 
    ex3()
if choice == 4:
    ex4()
if choice == 5:
    ex5()

