from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

mapped = list(map(lambda x: x * 3, numbers))

filtered = list(filter(lambda x: x % 2 != 0, numbers))

reduced = reduce(lambda a, b: a * b, numbers)

print("Original:", numbers)
print("Map:", mapped)
print("Filter:", filtered)
print("Reduce:", reduced)