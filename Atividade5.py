# Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
