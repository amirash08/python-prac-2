#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
#Test if a is greater than b, AND if c is greater than a, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b and c > a or a > c:
    print("At least one of the conditions is True")

    