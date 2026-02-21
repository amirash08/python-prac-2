# inheritance_basics.py
# 4 examples: parent-child relationships

print("\n--- Example 1: child inherits method ---")
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

Dog().speak()


print("\n--- Example 2: child inherits __init__ ---")
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Amir")
print(s.name)


print("\n--- Example 3: child adds new method ---")
class Car:
    def drive(self):
        print("Driving")

class ElectricCar(Car):
    def charge(self):
        print("Charging")

e = ElectricCar()
e.drive()
e.charge()


print("\n--- Example 4: isinstance check ---")
class A: pass
class B(A): pass
b = B()
print(isinstance(b, B))
print(isinstance(b, A))