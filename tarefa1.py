largura = float(input("qual a largura do local?: "))
altura = float(input("qual a altura do local ?: "))
area: float = largura * altura
tinta: float = (largura * altura)//6

if tinta <= 18:
    print ("quantidade nescessaria: 1 lata de 18 litros")
    print ("R$ 80.00")
else:
    latas: int = tinta//18
    print("a quantidade de latas de 18 litros é" ,latas)
    print ("o valor será de: R$" , latas * 80.00 )
if tinta <= 3.6:
    print ("quantidade nescessaria: 1 galão de 3,6 litros")
    print ("valor R$ 25.00")
else:
    galao: int = tinta//3.6
    print ("a quantidade de galões de 3,6 litros é" , galao)
    print (" o valor será de: R$" , galao * 25.00)




    