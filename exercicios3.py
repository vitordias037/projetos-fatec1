num1: int
num2: int
num3: float
resultado1: int
resultado2: int
resultado3: float
resultado4: float

num1 = int(input("digite o numero 1: "))
num2 = int(input("digite o numero 2: "))
num3 = float(input("digite o numero 3: "))

resultado1 = num1 *2 + num2/2
# ---------------------------------------------------------------
resultado2 = num1 * 3 + num3
# ------------------------------------------------------------------
resultado3 = num3 **3
# -------------------------------------------------------------------
resultado4 = num2 ** (1/3)
print(resultado1 , resultado2 , resultado3 , resultado4)