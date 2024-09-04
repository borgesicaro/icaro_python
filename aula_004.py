carros=['fox', 'polo', 'gol', 'up', 'corola']#lista

carros.append(0,'camaro')#adicionar item a lista, o 0 direciona para a posição na lista, é opcional
carros.remove=('up')#remove o item selecionado
print(carros)

#para passaar um número de string para número
n1= int(input('escolha um número'))
n2= int(input('escolha outro número')) # o int(...)  é colocado para mostrar que é um número e não um texto
print(n1+n2)


#string são listas de caracteres
nome='icaro'

print(nome[2])# no caso irá mostrar o terceiro caráctere

#contador de carcteres
def contador():
    palavra=input('escreva aqui sua palavra')
    qtd_carac=(len(palavra))
    print(qtd_carac)


    contador('icaro')


    #replace
    #         texto.replace('krl', '**') # troca a primeira string pela segunda