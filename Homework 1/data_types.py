# 1) str (строка)
x = str("Hello World")
print(type(x))

# 2) int (целое число)
x = int(20)
print(type(x))

# 3) float (число с точкой)
x = float(20.5)
print(type(x))

# 4) complex (комплексное число)
x = complex(1j)
print(type(x))

# 5) list (список)
x = list(("apple", "banana", "cherry"))
print(type(x))

# 6) tuple (кортеж)
x = tuple(("apple", "banana", "cherry"))
print(type(x))

# 7) range (диапазон)
x = range(6)
print(type(x))

# 8) dict (словарь)
x = dict(name="John", age=36)
print(type(x))

# 9) set (множество)
x = set(("apple", "banana", "cherry"))
print(type(x))

# 10) frozenset (неизменяемое множество)
x = frozenset(("apple", "banana", "cherry"))
print(type(x))

# 11) bool (логический тип)
x = bool(5)
print(type(x))

# 12) bytes (байты)
x = bytes(5)
print(type(x))

# 13) bytearray (изменяемые байты)
x = bytearray(5)
print(type(x))

# 14) memoryview (представление памяти)
x = memoryview(bytes(5))
print(type(x))
