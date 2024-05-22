soma:float = 0
continuasoma = True

while continuasoma == True:
    print("a soma está no valor de :", soma)

    opcao:str = input("quer continuar a soma  (S | N)")


    if opcao == "s":
        num:float = float(input("digite o numero"))
        soma = soma + num
    else:
        continuasoma = False
            
print("total somado é: ", soma)
    
            



