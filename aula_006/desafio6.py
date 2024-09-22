def media(a, b, c):
    return f"A média dos numeros é {(a+b+c)/3}"

n1=int(input('escolha um número'))
n2=int(input('escolha um número'))
n3=int(input('escolha um número'))
print(media(n1, n2, n3))

def maior(a, b, c):
  if a>100 or b>100 or c >100:
     return True
  return False

  
if maior(n1, n2, n3):
    print("Um ou mais números fornecidos são maiores que 100.")
else:
    print("Nenhum dos números fornecidos é maior que 100.")
