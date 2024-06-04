palavra1: str = input("digite")
tamanho: int = len(palavra1)

p: int = tamanho - 1
palavra2: str =""

while p >= 0:
    palavra2 = palavra2 + (palavra1[p])
    p = p - 1

if palavra1 == palavra2:
    print("é palindromo")
else:
    print("não é palindromo")