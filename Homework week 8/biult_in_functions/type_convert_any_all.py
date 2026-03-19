values = ["123", 0, 5.7, True]

for value in values:
    print(value, "->", type(value))

text_number = "456"
converted_int = int(text_number)
converted_float = float("12.5")
converted_str = str(999)

print("\nConverted values:")
print(converted_int, type(converted_int))
print(converted_float, type(converted_float))
print(converted_str, type(converted_str))

numbers1 = [1, 2, 3]
numbers2 = [0, 0, 4]

print("\nall(numbers1):", all(numbers1))
print("any(numbers2):", any(numbers2))