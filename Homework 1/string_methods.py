# Демонстрация основных методов строк (Python String Methods)
# Каждый блок: что делает метод + пример

s = "hello world"
s2 = "  Hello, World!  "
nums = "12345"
mix = "Hello123"
space = "   "

print("Исходные строки:")
print("s =", s)
print("s2 =", repr(s2))  # repr показывает пробелы
print()

# capitalize() — делает первую букву заглавной, остальное маленьким
print("capitalize:", s.capitalize())

# casefold() — сильное приведение к нижнему регистру (для сравнения)
print("casefold:", "Straße".casefold())

# center(width, fill) — центрирует строку
print("center:", s.center(20, "-"))

# count(sub) — сколько раз подстрока встречается
print("count:", s.count("l"))

# encode() — кодирует строку в bytes (по умолчанию utf-8)
print("encode:", "привет".encode("utf-8"))

# endswith(suffix) — заканчивается ли строка на suffix
print("endswith:", s.endswith("world"))

# expandtabs(tabsize) — заменяет \t на пробелы по табуляции
print("expandtabs:", "a\tb\tc".expandtabs(4))

# find(sub) — индекс первого вхождения или -1
print("find:", s.find("world"))

# format() — подставляет значения в шаблон
print("format:", "My name is {} and I'm {}".format("Amir", 18))

# format_map(dict) — как format, но подставляет из словаря
data = {"name": "Amir", "age": 18}
print("format_map:", "Name: {name}, Age: {age}".format_map(data))

# index(sub) — как find, но если нет — ошибка
print("index:", s.index("world"))

# isalnum() — только буквы/цифры (без пробелов)
print("isalnum:", mix.isalnum())

# isalpha() — только буквы
print("isalpha:", "Hello".isalpha())

# isascii() — только ASCII символы
print("isascii:", "Hello!".isascii())

# isdecimal() — десятичные цифры
print("isdecimal:", nums.isdecimal())

# isdigit() — цифры (шире чем decimal)
print("isdigit:", nums.isdigit())

# isidentifier() — можно ли использовать как имя переменной
print("isidentifier:", "my_var".isidentifier())

# islower() — все буквы в нижнем регистре?
print("islower:", s.islower())

# isnumeric() — числовая строка (шире чем digit)
print("isnumeric:", nums.isnumeric())

# isprintable() — все символы печатные?
print("isprintable:", "Hello\n".isprintable())

# isspace() — только пробельные символы?
print("isspace:", space.isspace())

# istitle() — заглавные первые буквы слов?
print("istitle:", "Hello World".istitle())

# isupper() — все буквы в верхнем регистре?
print("isupper:", "HELLO".isupper())

# join(iterable) — соединяет элементы через строку-разделитель
print("join:", "-".join(["a", "b", "c"]))

# ljust(width, fill) — выравнивание влево
print("ljust:", "hi".ljust(10, "."))

# lower() — в нижний регистр
print("lower:", "HeLLo".lower())

# lstrip(chars) — убрать пробелы/символы слева
print("lstrip:", s2.lstrip())

# maketrans() + translate() — замена символов по таблице
table = str.maketrans({"H": "h", "W": "w", "!": "?"})
print("translate:", "Hello World!".translate(table))

# partition(sep) — делит на 3 части: до, sep, после
print("partition:", "a=b=c".partition("="))

# replace(old, new) — заменяет подстроки
print("replace:", s.replace("world", "Python"))

# rfind(sub) — индекс последнего вхождения или -1
print("rfind:", "one two one".rfind("one"))

# rindex(sub) — как rfind, но если нет — ошибка
print("rindex:", "one two one".rindex("one"))

# rjust(width, fill) — выравнивание вправо
print("rjust:", "hi".rjust(10, "."))

# rpartition(sep) — как partition, но справа
print("rpartition:", "a=b=c".rpartition("="))

# rsplit(sep) — разбивает справа (обычно как split)
print("rsplit:", "a,b,c,d".rsplit(",", 2))

# rstrip(chars) — убрать пробелы/символы справа
print("rstrip:", s2.rstrip())

# split(sep) — разбить на список
print("split:", "a b  c".split())

# splitlines() — разбить по строкам
print("splitlines:", "a\nb\nc".splitlines())

# startswith(prefix) — начинается ли строка с prefix
print("startswith:", s.startswith("hello"))

# strip(chars) — убрать пробелы по краям (или указанные символы)
print("strip:", s2.strip())

# swapcase() — меняет регистр местами
print("swapcase:", "HeLLo".swapcase())

# title() — каждое слово с заглавной буквы
print("title:", "hello world".title())

# upper() — в верхний регистр
print("upper:", s.upper())

# zfill(width) — заполняет слева нулями до длины width
print("zfill:", "42".zfill(6))

# removeprefix(prefix) — убрать префикс (Python 3.9+)
print("removeprefix:", "unhappy".removeprefix("un"))

# removesuffix(suffix) — убрать суффикс (Python 3.9+)
print("removesuffix:", "filename.txt".removesuffix(".txt"))
