names = ["Amir", "Ali", "Dana"]
ages = [19, 20, 18]

print("Enumerate example:")
for index, name in enumerate(names):
    print(index, name)

print("\nZip example:")
for name, age in zip(names, ages):
    print(name, age)