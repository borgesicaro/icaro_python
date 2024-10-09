frutas=["maçã", "banana", "laranja", "uva", "morango"]
primeira_fruta=frutas[0]
ultima_fruta=frutas[-1]

print(primeira_fruta)
print(ultima_fruta)

frutas.remove(primeira_fruta)
frutas.remove(ultima_fruta)

primeira=(input("coloque outra fruta/ "))

frutas.insert(0, primeira)

frutas.append(input("coloque outra fruta/ "))

print(frutas[0])
print(frutas[-1])