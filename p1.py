num1: float
num2: float
num3: float

num1 = float(input("digite o lado1: "))
num2 = float(input("digite o lado2: "))
num3 = float(input("digite o lado3: "))

if (num1 == num2) and (num1 == num3) and (num2 == num3):
    print ("triangulo equilátero")
elif num1 == num2 or (num1 == num3) or (num2 == num3):    
    print("triangulo isósceles")
else:
    print ("triangulo escaleno")    