# Gerador de Senhas
import random
import string

print("\n--- Gerador de Senhas ---")

comprimento = int(input("Digite o comprimento da senha: "))

if comprimento <= 0:
    print("Comprimento inválido. A senha deve ter pelo menos 1 caractere.")
else:
    print("\nQuais tipos de caracteres deseja incluir?")
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower() == "s"
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == "s"
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == "s"

    caracteres = ""

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("\nErro: selecione pelo menos um tipo de caractere.")
    else:
        senha = "".join(random.choice(caracteres) for _ in range(comprimento))
        print(f"\nSenha gerada: {senha}")
