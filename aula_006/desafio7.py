def pares(*numeros):
    lista=[]
    for num in numeros:
     if num%2==0:
        lista.append(num)
    return lista


def soma(n):
   return sum(n)


n1=int(input('escolha um número'))
n2=int(input('escolha um número'))
n3=int(input('escolha um número'))

num_pares=pares(n1, n2, n3)
print(f" Os números pares são {pares(n1, n2, n3)}")
print(f"A soma dos números pares é {soma(num_pares)}")