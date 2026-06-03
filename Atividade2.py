# Calculadora simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"\nSoma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {divisao}")
else:
    print("Divisão: não é possível dividir por zero")
