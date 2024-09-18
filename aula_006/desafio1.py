
def tmp_past (name, age):
 temp=100-age
 ano=2024+temp
 return f"{name} terá 100 anos em {ano}"

nome=input('qual é o seu nome ?')
idade=int(input('quantos anos você tem ?'))
msg=tmp_past(nome, idade)

linhas=int(input('insira um número'))
i=1
while (i<=linhas):
 print(msg)
 i=i+1