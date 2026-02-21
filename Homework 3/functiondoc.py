def add(a,b ):
    """Returns the sum of two numbers."""
    return a + b 
print(add.__doc__)

def area_circle(r):
    return 3.14*r*r 
print(area_circle) 

def greet(name):
    """
    Prints Hello message"""

    print("Hello," , name)
print(greet.__doc__)

def is_even(n):
    return n%2==0
print  (is_even(10))
