lista:int = [1, 2, 5, 7, 10, 99, 66]
contador:int = 0
maxi:int = lista[0]


while contador <= len(lista) - 1:
    if maxi < lista[contador]:
        maxi = lista[contador]
    contador = contador + 1
 
print(maxi)


