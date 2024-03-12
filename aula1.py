numero1: int = 10
num2: float = 10.5
ligadesliga: bool = True
text: str = "Hello World"

# comentar

print (numero1) 
print (num2)
print (text) 
print (ligadesliga)
# ou separar por virgula exemplo "print (num2, text, numero1, ligadesliga)"
# pode se escrever entre as virgulas exemplo ( num2, "testo que quero escrever", numero1)
print (text, "--", num2)
print ("o numb2 vale :" + str(num2))
# -------------------------------------------------------------------------------------------------------------------
primeiro_nome: str = "vitor"
segundo_nome: str = "dias"
nome_completo: str = primeiro_nome + " " + segundo_nome

print (nome_completo)
# primeiroNome camelcase
# primeiro_nome snake case
# ========================================================================================================================
primeiro_num: int = 9
segundo_num: int = 2
soma: int = primeiro_num + segundo_num
print (soma)
# ========================================================================================================================

resultado: int = primeiro_num - segundo_num
print (resultado)

resultado: int = primeiro_num * segundo_num
print (resultado)

resultado: float = primeiro_num / segundo_num # float por que pode ser numero quebrado exemplo 1 quarto ou 1,5
print (resultado)

resultado: float = primeiro_num ** segundo_num #potencia
print (resultado)

resultado: float = primeiro_num ** (1 / segundo_num) # raiz quadrada
print(resultado)
# =============================================================================================================================
num: int = 1
num2: int = 2
resultado: int = num + num2
print (resultado)
# ==============================================================================================================================

num1: int = input ("informe o numero: ")
print (num1)
# ===============================================================================================================================
# ===========================Calculadora=================================================================================
num1: int = int(input ("informe o numero1: ") )
num2: int = int(input ("informe o numero2: ") )
nume3: int = int(input ("informe o numero3: ") )
soma: int =  num1 +  num2
print (soma)
# ==============================================================================================================================

nota1: float 
nota2: float
nota3: float
media: float

nota1 = float(input("digite a nota 1: ") ) 

nota2 = float(input("digite a nota 2: ") )

nota3 = float(input("digite a nota 3: ") )

media = (nota1 + nota2 + nota3) /3
print (media)
# conteudo das aulas github.com/yurimagagnatto/algoritmos-python