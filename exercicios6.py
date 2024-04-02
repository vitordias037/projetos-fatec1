
print("1 - quadradro")
print("2 - triangulo isósceles")
print("3 - circulo")
print("4 - retangulo")

forma = input(("escolha a forma geométrica:"))

if forma == "1" or forma == "quadrado":
    lado1 = float(input("digite o lado 1: "))
    lado2 = float(input("digite o lado 2: "))
    print ("area é:" ,lado1 * lado2)
elif forma == "2" or forma == "triangulo isósceles":
    base = float(input("digite a base do triangulo isósceles: "))
    altura = float(input("digite a altura do triangulo isósceles: "))
    print ("area é:" , (base * altura)/2)
elif forma == "3" or forma == "circulo":
    pi: float = 3.14
    raio = float(input("digite o raio do circulo: "))
    print ("area é:" ,  (pi * raio) ** 2)
elif forma == "4" or forma == "retangulo":
    base = float(input("base do retangulo"))
    altura = float(input("altura do retangulo"))
    print("area é:" , base * altura)



