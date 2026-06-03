# Leitor de Arquivo de Texto
nome_arquivo = input("Digite o nome do arquivo (.txt): ")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("\n--- Conteúdo do arquivo ---")
        print(conteudo)
except FileNotFoundError:
    print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado.")
