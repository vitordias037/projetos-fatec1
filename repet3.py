a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))


if a <=b:
    for x in range(a , (b+1)):
     for i in range(0, 11):
        print (x * i)
else:
    for x in range(b , (a+1)):
     for i in range(0, 11):
        print (x * i)     

        