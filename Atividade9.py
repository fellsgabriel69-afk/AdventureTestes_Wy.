# Fatorial de um Número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("O fatorial só é definido para números inteiros não negativos.")
else:
    resultado = fatorial(numero)
    print(f"\nFatorial de {numero} = {resultado}")
