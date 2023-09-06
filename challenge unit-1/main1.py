#Implement a recursive function to calculate the factorial of a given number.
def f_number(num):
  if num==0 or num==1:
    return 1
  else:
    return num*f_number(num-1)

num = int(input("Enter a Number :"))
result = f_number(num)
print("The factorial of {} is {}".format(num,result))