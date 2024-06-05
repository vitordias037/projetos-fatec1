lista:int = [1, 5, 7, 8]
lista2:int = [6, 2, 1, 4,]
lista3: int = []
# lista3.append / .append e pra adicionar o numero na lista 3 que está vazia
contador:int = 0

while contador <= len(lista) - 1:
    lista3.append(lista[contador])
    lista3.append(lista2[contador])
    contador = contador + 1

print(lista3)
