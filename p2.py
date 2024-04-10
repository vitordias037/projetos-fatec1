data: int

data = int(input("digite o ano"))
print( data % 4, data % 400 , data %100)
if (data % 4 == 0 and data % 100 >=1) or data % 400 == 0:
    print ("este ano é bisexto")
else:
    print("este ano não é bisexto")    