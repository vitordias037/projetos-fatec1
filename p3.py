num1: float
num2: float
num3: float

num1 = float(input(" valor 1:"))
num2 = float(input(" valor 2:"))
num3 = float(input(" valor 3:"))

if num1 > num2 and num1 > num3:
    print (num1)
elif num2 > num1 and num2 > num3:
    print (num2)
else:
    print (num3)
    