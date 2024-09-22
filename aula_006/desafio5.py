def eh_palindromo(palavra):
    
    palavra_limpa = palavra.replace(" ", "").lower()
    
    return palavra_limpa == palavra_limpa[::-1]


palavra_usuario = input("Digite uma palavra: ")


if eh_palindromo(palavra_usuario):
    print(f"'{palavra_usuario}' é um palíndromo!")
else:
    print(f"'{palavra_usuario}' não é um palíndromo.")