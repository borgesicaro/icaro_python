def numero(n):
    if n<0:
        print(f'{n} é negativo')
    elif n>0 and n%2==0:
        print(f'{n} é positivo par ')
    elif n>0 and n%2!=0:
        print(f"{n} é positivo impar")
    else:
        print(f'{n} igual a zero')



num=int(input("Escolha um número"))

numero(num)






""" Escreva um programa que receba três números inteiros como entrada e determine qual é o maior deles usando estruturas if aninhadas. """

def maior (a, b, c):
    if a>b and a>c:
        print(f"{a} é maior entre os três")
    elif b>a and b>c:
        print(f"{b} é maior entre os três")
    else:
        print(f"{c} é maior entre os três")

n1=int(input("Escolha um número"))
n2=int(input("Escolha um número"))
n3=int(input("Escolha um número"))

maior(n1, n2, n3)







"""  Um aluno precisa de nota mínima 60 em três provas para ser aprovado. Se a média for maior que 70, ele passa com distinção. Escreva um programa que leia as três notas e, utilizando estruturas if aninhadas, determine se o aluno foi reprovado, aprovado ou aprovado com distinção. """

def nota (d, e, f):
 media=int((d+e+f)/3)
 if media>70:
  print(f"sua média foi de {media} você passou com distinção")
 elif media>=60 and media<70:
  print(f"sua média foi de {media} você passou")
 else:
  print(f"sua média foi de {media} reprovado")

n4=int(input("insira sua primeira nota"))
n5=int(input("insira sua segunda nota"))
n6=int(input("insira sua terceira nota"))

nota(n4, n5, n6)








"""  Escreva um código em Python que receba a idade de uma pessoa e determine a categoria em que ela se encaixa:
Menor de 12 anos: "Criança"#
De 12 a 17 anos: "Adolescente"
De 18 a 64 anos: "Adulto"
Acima de 64 anos: "Idoso" Utilize estruturas if aninhadas. """

def faixa_etaria(idade):
    if idade<12:
        print("criança")
    elif idade==12 and idade<=17:
        print('adolecente')
    elif idade>=18 and idade<=64:
        print('adulto')
    else:
        print('idoso')

anos=int(input("qual é asua idade ?"))
faixa_etaria(anos)





""" Escreva um programa que leia um número e verifique se ele é divisível por 2, 3 ou ambos. Use estruturas if aninhadas para tratar os diferentes casos e exibir a mensagem apropriada. """

def div(l):
    if l % 2==0 and l % 3==0:
        print(f"seu numero é divisível por 2 e 3")
    elif l % 3==0:
        print(f"seu numero é divisível por 3")
    elif l % 2==0:
        print(f"seu numero é divisível por 2")

number=int(input("escolha um número"))
div(number)













""" Dada uma lista lista_original = [1, 2, 3, 4, 5], escreva um código que crie uma cópia dessa lista usando a função list() e modifique o primeiro elemento da lista clonada para 10. Mostre as duas listas para verificar se a original permaneceu inalterada. """

def list(lista):
    lista=[1, 2, 3, 4, 5]
    print(lista)
    lista.insert(0,10)
    print(lista)

lista_original = [1, 2, 3, 4, 5]
list(lista_original)





nomes=[]
for i in range(5):
 nome=(input("insira um nome"))
 nomes.append(nome)

copia = nomes[:]

print(copia)
print(nomes)





numeros = [10, 20, 30, 40]
copia= numeros.copy()

copia[-1] = 99

print(numeros)
print(copia)








lista01=[1, 2, 3, 4, 5]

listaigual= lista01
print(listaigual)

listacopia= lista01.copy()
print(listacopia)

listafatia= lista01[:]
print(listafatia)









itens = ["maçã", "banana", "laranja"]

print(itens)

itenscopy= itens.copy()

itenscopy.insert(1, 'melancia')

print(itenscopy)