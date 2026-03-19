# Example 2: read file and append new text

with open("example2.txt", "w", encoding="utf-8") as file:
    file.write("Old line 1\n")
    file.write("Old line 2\n")

with open("example2.txt", "r", encoding="utf-8") as file:
    print("Before append:")
    print(file.read())

with open("example2.txt", "a", encoding="utf-8") as file:
    file.write("New appended line\n")

with open("example2.txt", "r", encoding="utf-8") as file:
    print("After append:")
    print(file.read())