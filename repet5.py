num = int(input("digite o numero"))
if num == 2:
    print("primo")
else:
    for i in range (1, num+1):
        x = 0
        for a in range(1, i+1):
            if (i % a == 0):
            
                x = x+1
        if x ==2:
            print(i, "é primo")
        else:
            print(i, "nao e primo")    