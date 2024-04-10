num1: float
num2: float
num3: float

num1 = float(input(" valor 1:"))
num2 = float(input(" valor 2:"))
num3 = float(input(" valor 3:"))

if num1 >= num2 and num2 >= num3:
    print (num3 , num2 , num1)
elif num2 >= num1 and num1 >= num3:
    print (num3 , num1 , num2)
elif num3 >= num2 and num2 >= num1:
    print (num1 , num2 , num3)
elif num1 >= num3 and num3 >= num2:
    print (num2 , num3 , num1)
elif num2 >= num1 and num3 >= num1:
    print (num1 , num3 , n2)
else num3 >= num2 and num1 >= num2:
    print (num2 , num1 , num3)