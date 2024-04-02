num1: float 
num2: float
operacao: str
print("1 - adição:")
print("2 - subtração:")
print("3 - multiplicação:")
print("4 - divisão:")

operacao = input("digite a opção desejada: ")
num1 = float (input(" digite o numero 1: "))
num2 = float (input(" digite o numero 2: "))

if operacao == "1" or  operacao == "adição":
    print (num1 + num2)
# adição
elif operacao == "2" or operacao == "subtração":
    print (num1 - num2)
# subtrção
elif operacao == "3" or operacao == "multiplicação":
    print (num1 *  num2)
# multiplicação
elif operacao == "4" or operacao == "divisão":
    print (num1  / num2)
# divisão
else:
    print("você não digitou uma opção valida, tente novamente: ")