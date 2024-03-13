valorH: float
horasM: float
salario: float
impostorenda:float
inss: float
sindicato: float
salariolivre: float

valorH = float(input("digite o valor ganho por Hora") )
horasM = float(input("digite a quantidade de Horas trabalhadas"))
salario = horasM * valorH
impostorenda = (salario * 11) /100
inss = (salario * 8) / 100
sindicato = (salario * 5) / 100

salariolivre = (salario - impostorenda - inss - sindicato)
print("salario Bruto: ",salario)
print("IR: ", impostorenda)
print("INSS: ",inss)
print("sindicato: ",sindicato)
print("salario liquido",salariolivre)

