# Write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statements.

def leapyear(y):
  if(y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    return True
  else:
    return False
 

y = int(input("Enter a year :"))

if leapyear(y):
  print("{} is a Leap Year.".format(y))
else:
  print("{} is not a Leap Year.".format(y))