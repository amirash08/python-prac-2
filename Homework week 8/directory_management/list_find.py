import os

print("All items in current directory:")
for item in os.listdir("."):
    print(item)

print("\nPython files:")
for item in os.listdir("."):
    if item.endswith(".py"):
        print(item)