# Análise de Dados Simples (CSV)
import csv
import os

ARQUIVO_CSV = "vendas.csv"
CABECALHO = ("produto", "quantidade", "preco")


def garantir_arquivo():
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
            csv.writer(arquivo).writerow(CABECALHO)


def carregar_vendas():
    garantir_arquivo()
    with open(ARQUIVO_CSV, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def salvar_vendas(vendas):
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHO)
        escritor.writeheader()
        escritor.writerows(vendas)


def listar_vendas(vendas):
    if not vendas:
        print("\nNenhum produto cadastrado.")
        return

    print("\n--- Vendas cadastradas ---")
    for indice, linha in enumerate(vendas, start=1):
        produto = linha["produto"]
        quantidade = linha["quantidade"]
        preco = linha["preco"]
        subtotal = int(quantidade) * float(preco)
        print(
            f"{indice}. {produto} | "
            f"qtd: {quantidade} | "
            f"preço: R$ {float(preco):,.2f} | "
            f"subtotal: R$ {subtotal:,.2f}"
        )


def adicionar_venda(vendas):
    produto = input("Nome do produto: ").strip()
    if not produto:
        print("O nome do produto não pode estar vazio.")
        return vendas

    try:
        quantidade = int(input("Quantidade: ").strip())
        preco = float(input("Preço unitário: ").strip().replace(",", "."))
    except ValueError:
        print("Quantidade e preço devem ser números válidos.")
        return vendas

    if quantidade <= 0 or preco < 0:
        print("Quantidade deve ser maior que zero e o preço não pode ser negativo.")
        return vendas

    vendas.append(
        {
            "produto": produto,
            "quantidade": str(quantidade),
            "preco": f"{preco:.2f}",
        }
    )
    salvar_vendas(vendas)
    print("Produto adicionado com sucesso.")
    return vendas


def remover_venda(vendas):
    if not vendas:
        print("\nNão há produtos para remover.")
        return vendas

    listar_vendas(vendas)
    try:
        indice = int(input("\nNúmero do item a remover (0 para cancelar): ").strip())
    except ValueError:
        print("Informe um número válido.")
        return vendas

    if indice == 0:
        print("Remoção cancelada.")
        return vendas

    if indice < 1 or indice > len(vendas):
        print("Número inválido.")
        return vendas

    removido = vendas.pop(indice - 1)
    salvar_vendas(vendas)
    print(f"Removido: {removido['produto']}")
    return vendas


def analisar_vendas(vendas):
    if not vendas:
        print("\nCadastre vendas antes de analisar.")
        return

    total_vendas = 0.0
    quantidade_por_produto = {}

    for linha in vendas:
        produto = linha["produto"].strip()
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco"])

        total_vendas += quantidade * preco
        quantidade_por_produto[produto] = (
            quantidade_por_produto.get(produto, 0) + quantidade
        )

    produto_mais_vendido = max(
        quantidade_por_produto, key=quantidade_por_produto.get
    )
    unidades = quantidade_por_produto[produto_mais_vendido]

    print("\n--- Resultado da análise ---")
    print(f"Total de vendas: R$ {total_vendas:,.2f}")
    print(f"Produto mais vendido: {produto_mais_vendido} ({unidades} unidades)")


print("\n--- Análise de Dados Simples (CSV) ---")
print(f"Os dados ficam salvos em '{ARQUIVO_CSV}'")
print("Você pode adicionar ou remover produtos quando quiser.\n")

vendas = carregar_vendas()

while True:
    print("\nMenu:")
    print("1 - Listar vendas")
    print("2 - Adicionar produto")
    print("3 - Remover produto")
    print("4 - Calcular total e produto mais vendido")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        listar_vendas(vendas)
    elif opcao == "2":
        vendas = adicionar_venda(vendas)
    elif opcao == "3":
        vendas = remover_venda(vendas)
    elif opcao == "4":
        analisar_vendas(vendas)
    elif opcao == "5":
        print("\nEncerrando o programa.")
        break
    else:
        print("Opção inválida.")
