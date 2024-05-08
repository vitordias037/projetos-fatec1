# Inicializando a lista de vendas vazia
vendas = []

# Solicitando os valores das vendas ao usuário
while True:
    valor_venda = input("Digite o valor da venda (ou digite 'fim' para terminar): ")
    
    # Verificando se o usuário deseja encerrar a entrada de vendas
    if valor_venda.lower() == 'fim':
        break
    
    # Convertendo o valor da venda para float e adicionando à lista de vendas
    vendas.append(float(valor_venda))

# Calculando a receita total
receita_total = sum(vendas)

# Exibindo o resultado
print("A receita total do dia é:", receita_total)
entrada: float
gastos: float = 0
plataforma: str
lucro: float

plataforma = (input("digite ifood ou aiq: "))
entregas = input("digite barra ou igaraçu: ")

if entregas == "barra":
    gastos + 8
else:
    gastos + 9 

if plataforma == "aiq":
    taxa = (receita_total*15)/100
else:
    taxa = (receita_total*17/100)

lucro = (receita_total - taxa - gastos)
print(lucro)





