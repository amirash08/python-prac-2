sq = lambda x: x*x
prin(sq(5)) 

add + lambda a, b:a+ b 
print(add(2,3))

is_even = lambda n: n % 2 == 0
print(is_even(10))

print((lambda s; s.upper())("amir""))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)