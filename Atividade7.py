# Contador de Vogais
def contar_vogais(texto):
    vogais = "aeiou"
    return sum(1 for letra in texto.lower() if letra in vogais)


texto = input("Digite um texto: ")
quantidade = contar_vogais(texto)
print(f"\nNúmero de vogais: {quantidade}")
