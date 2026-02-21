import json
# a JSON string:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
#print(y)
print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json  # импортируем модуль json (работа с JSON)

# 1) Python -> JSON (json.dumps)
data = {                     # обычный словарь Python
    "name": "Amir",          # строка
    "age": 18,               # число
    "is_student": True,      # bool
    "scores": [90, 85, 100]  # список
}

json_text = json.dumps(data)           # превращаем словарь в JSON-строку
print(json_text)                       # печатаем JSON-строку

pretty = json.dumps(data, indent=2)    # красивый JSON с отступами
print(pretty)                          # печатаем красивый JSON

# 2) JSON -> Python (json.loads)
text = '{"city":"Almaty","temp":-5,"rain":false}'  # JSON-строка
obj = json.loads(text)                              # превращаем JSON-строку в словарь Python
print(obj)                                          # печатаем словарь
print(obj["city"])                                  # берём значение по ключу "city"

# 3) Запись JSON в файл (json.dump)
with open("data.json", "w", encoding="utf-8") as f:  # открываем файл для записи
    json.dump(data, f, ensure_ascii=False, indent=2)  # записываем data в файл как JSON

# 4) Чтение JSON из файла (json.load)
with open("data.json", "r", encoding="utf-8") as f:  # открываем файл для чтения
    loaded = json.load(f)                              # читаем JSON из файла в словарь Python
print(loaded)                                          # печатаем то, что прочитали