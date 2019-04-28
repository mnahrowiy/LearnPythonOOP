import math
x= int(input("Enter a Value For x : "))
y= int(input("Enter a Value For y : "))

if y is 1 or y is x:
    print(1)

if y > x:
    print(0)
else:
    a = math.factorial(x)
    b = math.factorial(y)
    div = a // (b*(x-y))
    print(div)
