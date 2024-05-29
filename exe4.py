lista = [10, 15, 20, 25, 30, 40, 50, 25]
num: int = int(input("digite o numero desejado"))
num2: int = 0
for i in range (0, len(lista)):
    
    if lista[i]== num:
        num2 = num2 + 1
        
print ("foram achadas", num2, "vezes")
