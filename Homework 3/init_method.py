print("\n--- Extra Example 5: init + method uses attributes ---")
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def info(self):
        print(self.title, "-", self.pages, "pages")

b = Book("Python Basics", 120)
b.info()

print("\n--- Extra Example 7: init creates derived attribute ---")
class Circle:
    def __init__(self, r):
        self.r = r
        self.area = 3.14159 * r * r  # вычислили сразу

c = Circle(3)
print("r:", c.r, "area:", c.area)

print("\n--- Extra Example 8: init with simple validation ---")
class User:
    def __init__(self, username):
        username = username.strip()
        if username == "":
            username = "guest"
        self.username = username

u1 = User("   Amir   ")
u2 = User("   ")
print(u1.username)  # Amir
print(u2.username)  # guest