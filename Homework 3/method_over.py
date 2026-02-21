
print("\n--- Example 1: super() in __init__ ---")
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

st = Student("Amir", 1)
print(st.name, st.grade)


print("\n--- Example 2: super() to extend method ---")
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

Dog().speak()


print("\n--- Example 3: super() with returned value ---")
class Base:
    def calc(self, x):
        return x + 1

class Child(Base):
    def calc(self, x):
        return super().calc(x) * 10

print(Child().calc(5))  # 60


print("\n--- Example 4: chain inheritance super() ---")
class A:
    def hello(self):
        print("A")
class B(A):
    def hello(self):
        super().hello()
        print("B")
class C(B):
    def hello(self):
        super().hello()
        print("C")

C().hello()