#saque
def saque(vlratual,vretirado):
    novo_valor=vlratual-vretirado
    return f'foi retirado R${vretirado}  e agora seu saldo é de R${novo_valor}'
print(saque(600, 100))

saque(600, 100)

#area
def circulo(raio):
    area=3.14*raio**2
    return f"A área do circulo é {area}"
print( circulo(3))

#fla funçãocom lista
def fila(fila_clientes):
    
    proximo_cliente=(fila_clientes[0])
    fila_clientes.remove(proximo_cliente[0])
    print(f"Cliente:{proximo_cliente[0]}")
    print(f"Proximos clientes  {fila_clientes}")

    fila(['icaro, rome, sandir, man'])

def soma(a, b):
    a=int(input('escolha um número'))
    b=int(input('escolha outro número'))
    resposta=a+b
    print(f'A soma de {a}+{b} é {resposta}')

soma(20, 30)

#condições
def impar_par(numero):
     if numero % 2==0:
      print('par')
     else:
      print('impar')


impar_par(20125693247632)


def div_3(n):
     if n%3==0:
      print(f"{n} é divisível por 3")
     else:
      print(f"{n} não é divisivel por 3")

div_3(63)