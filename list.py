lista = [-3, 10, -27, 38, 7, -5]
lista2 = []

contador:int = 0

while contador <= len(lista)-1:
    atual:int = lista[contador]
    if atual >= 0:
        lista2.append(atual)
    contador = contador +1
print(lista2)