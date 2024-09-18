def impar(n):
    if n %4 ==0:
        print(f'{n} é multiplo de 4')
    elif n % 2==0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')

num=int(input("Escolha um número"))
impar(num)

def div(n1,n2):
    if n1%n2==0:
        print(f"{n1} é divisivel por {n2} e o resultado é {n1/n2}")
    else:
        print(f"{n1} não é divisivel por {n2} e o resultado é {n1/n2}")


num1=int(input("escolha um número"))
num2=int(input("escolha outro número"))

div(num1, num2)