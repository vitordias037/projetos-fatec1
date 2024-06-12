senha = input("Digite sua senha: ")
special = ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':']

if len(senha) < 8 or len(senha) > 20:
    print("Senha inválida. A senha precisa ter de 8 a 20 caracteres.")
else:
    maius = False
    minus = False
    spec = False

    
    for char in senha:
        if char.isupper():
            maius = True
        elif char.islower():
           minus = True
        elif char in special:
           special = True

    
    if not maius:
        print("Senha inválida. A senha precisa ter pelo menos uma letra maiúscula.")
    elif not minus:
        print("Senha inválida. A senha precisa ter pelo menos uma letra minúscula.")
    elif not special:
        print("Senha inválida. A senha precisa ter pelo menos um caractere especial.")
    else:
        print("Senha válida!")
