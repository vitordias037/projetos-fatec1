p1:str = input("digite: ")
contador:int = 0


p2:str = ""
p3:str = ""

while contador <= len(p1) - 1:
    letratual:str = p1[contador]

    if letratual != " ":
        p2 = p2 + letratual
    
    contador = contador + 1
print(p2)

contador:int = len(p1) - 1
while contador >= 0:
    letratual:str = p1[contador]

    if letratual != " ":
        p3 = p3 + letratual
    contador = contador - 1 

if p2 == p3:
    print(p1, "é um palindromo")

print(p2, p3)