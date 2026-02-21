#The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

    day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

    #Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("It's a weekday")
  case 6 | 7:
    print("It's a weekend")

#You can add if statements in the case evaluation as an extra condition-check:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if day < 5:
    print("It's a weekday")
  case 6 | 7:
    print("It's a weekend")
    case :print("Looking forward to the Weekend")




