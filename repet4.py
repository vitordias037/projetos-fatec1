num = int(input("digite o numero"))
x: int = 0
if num == 2:
    print("primo")
else:
    for i in range (1, num+1):
        if (num % i == 0):
            
           x = x+1
    
                
    if x ==2:
        print("primo")
    else:
        print("nao e primo")    
    

    