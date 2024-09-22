def saudacao (name):
    return(f"Olá {name} Seja Bem Vindo")




def contagem(apelido):
    return len(apelido.replace(' ', ''))

nome=input("Qual é seu nome ?")
print(saudacao(nome))

print(f"Seu nome tem {contagem(nome)} letras")