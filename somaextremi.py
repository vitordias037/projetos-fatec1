lista = [10, 20, 50, 20, 30, 40]
lista2 = []

x:int = 0
y:int = len(lista)-1

while x < y:
    lista2.append(lista[x]+ lista[y])
    x=x+1
    y=y-1

print(lista2)




   

    

