# faça um programa que pergunte o quanto você ganha por hora, e quantas horas trabalhadas por mês, e calcule e mostre seu salario no mês

valorH: float
horasM: float
salario: float

valorH = float(input("digite o valor ganho por Hora") )
horasM = float(input("digite a quantidade de Horas trabalhadas"))
salario = horasM * valorH

total = "salario mensal R$:" + str(salario)

print(total)
