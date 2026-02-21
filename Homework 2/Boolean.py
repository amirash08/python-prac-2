print(10 > 9)
print(10 == 9)
print(10 < 9)
#print a message if the condition is true
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#This will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#Example 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#Print YES! if the function returns True, otherwise print NO!
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")