import re

text = "My phone number is 12345"

# Look for digits in the text
result = re.search(r"\d+", text)

# Check if we found something
if result:
    print("Found:", result.group())
else:
    print("No match")


import re

text = "cat bat rat mat"

# . means any one character
print(re.findall(r".at", text))   # matches cat, bat, rat, mat

# * means 0 or more repetitions
print(re.findall(r"ab*", "a ab abb abbb"))   # a, ab, abb, abbb

# + means 1 or more repetitions
print(re.findall(r"ab+", "a ab abb abbb"))   # ab, abb, abbb

# ? means 0 or 1 repetition
print(re.findall(r"ab?", "a ab abb"))   # a, ab, ab

# ^ means start of string
print(re.findall(r"^Hello", "Hello world"))   # Hello

# $ means end of string
print(re.findall(r"world$", "Hello world"))   # world

# [] means one character from a set
print(re.findall(r"[cr]at", "cat rat bat"))   # cat, rat

# | means OR
print(re.findall(r"cat|dog", "I like cat and dog"))   # cat, dog

# () groups parts together
print(re.findall(r"(ab)+", "ab abab ababab"))   # ab, ab, ab

import re

text = "Hello 123 \tWorld"

# \d = any digit
print(re.findall(r"\d", text))   # 1, 2, 3

# \w = letter, digit, or underscore
print(re.findall(r"\w", text))   # H, e, l, l, o, 1, 2, 3, W...

# \s = whitespace
print(re.findall(r"\s", text))   # spaces and tab

# \D = not a digit
print(re.findall(r"\D", "A1B2"))   # A, B

# \W = not a word character
print(re.findall(r"\W", "Hi! 123"))   # ! and space

# \S = not whitespace
print(re.findall(r"\S", "A B"))   # A, B

# \A = start of whole string
print(re.findall(r"\AHello", "Hello world"))   # Hello

# \Z = end of whole string
print(re.findall(r"world\Z", "Hello world"))   # world

import re

text = "cat bat mat rat 123"

# [abc] = one character: a, b, or c
print(re.findall(r"[cbm]at", text))   # cat, bat, mat

# [a-z] = lowercase letters
print(re.findall(r"[a-z]", "Hi123abc"))   # i, a, b, c

# [A-Z] = uppercase letters
print(re.findall(r"[A-Z]", "Hi123ABC"))   # H, A, B, C

# [0-9] = digits
print(re.findall(r"[0-9]", text))   # 1, 2, 3

# [^0-9] = anything except digits
print(re.findall(r"[^0-9]", "A1B2"))   # A, B

# [a-zA-Z0-9] = letters and digits
print(re.findall(r"[a-zA-Z0-9]", "Hi! 12"))   # H, i, 1, 2

import re

text = "My age is 19 and my friend's age is 21"

# search() finds the first match
result = re.search(r"\d+", text)

if result:
    print("First match:", result.group())
    print("Start position:", result.start())
    print("End position:", result.end())


import re

text = "I have 2 cats, 3 dogs, and 1 bird"

# findall() returns all matches as a list
numbers = re.findall(r"\d+", text)

print(numbers)

import re

text = "apple,banana;orange grape"

# Split by comma, semicolon, or space
parts = re.split(r"[,; ]+", text)

print(parts)

import re

text = "My phone is 123-456-789"

# Replace all digits with X
new_text = re.sub(r"\d", "X", text)

print(new_text)

import re

text = "Hello world"

# match() checks only from the start
result = re.match(r"Hello", text)

if result:
    print("Matched at beginning:", result.group())
else:
    print("No match")

import re

text = "hello\nWorld\nHELLO"

# IGNORECASE ignores letter case
print(re.findall(r"hello", text, re.IGNORECASE))   # hello, HELLO

# MULTILINE makes ^ and $ work line by line
print(re.findall(r"^hello", text, re.MULTILINE | re.IGNORECASE))   # hello, HELLO

