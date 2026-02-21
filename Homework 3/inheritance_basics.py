# class_variables.py
# 4 examples: class variables vs instance variables

print("\n--- Example 1: class variable shared ---")
class Cat:
    species = "cat"  # class variable
    def __init__(self, name):
        self.name = name

c1 = Cat("Murka")
c2 = Cat("Barsik")
print(c1.species, c2.species)


print("\n--- Example 2: changing class variable affects all ---")
Cat.species = "feline"
print(c1.species, c2.species)


print("\n--- Example 3: instance variable only for one object ---")
c1.species = "special cat"  # creates instance variable
print("c1:", c1.species)
print("c2:", c2.species)


print("\n--- Example 4: class counter ---")
class User:
    count = 0
    def __init__(self, name):
        self.name = name
        User.count += 1

u1 = User("A")
u2 = User("B")
u3 = User("C")
print("Total users:", User.count)