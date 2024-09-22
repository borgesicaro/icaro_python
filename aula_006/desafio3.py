def div (numero):
   
    divisores=[]
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

num=int(input("Escolha um número"))
resultado=div(num)
print(resultado)

def primo(numero):
    if numero % 4 != 0:
        print('primo') 
    elif numero % 3 ==0 or numero % 5 ==0:
        print(" Não primo")
    else:
        print('primo')


primo(num)