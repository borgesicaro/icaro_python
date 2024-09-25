""" def verifica_par(numero):
    if numero %2==0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

n=int(input("Escolha um número e descubra se é par ou impar"))
verifica_par(n) """




""" def maior_numero(n1, n2):
    if n1>n2:
        print(f"{n1} é maior que {n2}")
    elif n2>n1:
        print(f"{n2} é maior que {n1}")
    else:
        print("São números iguais")

num1=int(input("Escolha um número"))
num2=int(input("Escolha outro número"))
maior_numero(num1, num2) """



""" def verifica_positivo_negativo(num):
    if num>0:
        print("positivo")
    elif num<0:
        print("negativo")
    else:
        print("zero")
    

number=int(input("selecione um número"))
verifica_positivo_negativo(number) """



""" def e_maior_idade(idade):
    if idade>=18:
        print("Maior de idade")
    else:
        print("Menor de idade")

nam=int(input("Qual sua idade ?"))
e_maior_idade(nam) """


""" def nota_final(a, b, c):
    if (a+b+c)/3>=7:
        print(f"Sua média foi de {(a+b+c)/3} APROVADO")
    else:
        print(f"Sua média foi de {(a+b+c)/3} REPROVADO")

n5=float(input("Qual foi sua nota de português ?"))
n6=float(input("Qual foi sua nota de matemática ?"))
n7=float(input("Qual foi sua nota de georafia ?"))
nota_final(n5, n6, n7) """

def calcula_imposto(salario, dependentes):
    if salario<2000:
        print(f"você deve pagar R${200*dependentes},00")
    elif salario>2000 and salario<4000:
        print(f"Você deve pagar R${(2000*0.15)+(200*dependentes)},00")
    elif salario > 4000:
        print(f"Você deve pagar {(4000*0.275)+(200*dependentes)}")
    else:
        print(f"Você sonega imposto, safado")


sal=float(input("digite seu salario"))
dep=int(input("você tem quantos dependentes ?"))
calcula_imposto(sal, dep)