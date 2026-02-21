def greet (name="friend"):
    print ("Hello,", name )
greet()
greet(:"Amir")

def line(char="-", n=5):
    print(char * n)
line()
line("*", 3)

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)