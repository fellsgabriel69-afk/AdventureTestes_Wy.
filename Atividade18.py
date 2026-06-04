# Visualização de Dados com Matplotlib
import os

import matplotlib.pyplot as plt
import pandas as pd

ARQUIVO_CSV = "Clientes_atv16.csv"
COLUNAS = ("Nome", "Idade", "Cidade", "Renda")


def garantir_arquivo():
    if not os.path.exists(ARQUIVO_CSV):
        pd.DataFrame(columns=COLUNAS).to_csv(
            ARQUIVO_CSV, index=False, encoding="utf-8"
        )


def carregar_dados():
    garantir_arquivo()
    return pd.read_csv(ARQUIVO_CSV, encoding="utf-8")


def grafico_clientes_por_cidade(df):
    if df.empty:
        print("\nNenhum cliente cadastrado para gerar o gráfico.")
        return

    contagem = df["Cidade"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(contagem.index, contagem.values, color="steelblue", edgecolor="black")
    plt.title("Distribuição de Clientes por Cidade")
    plt.xlabel("Cidade")
    plt.ylabel("Quantidade de clientes")
    plt.tight_layout()
    plt.show()


def histograma_idades(df):
    if df.empty:
        print("\nNenhum cliente cadastrado para gerar o gráfico.")
        return

    plt.figure(figsize=(8, 5))
    plt.hist(
        df["Idade"],
        bins=range(int(df["Idade"].min()), int(df["Idade"].max()) + 2),
        color="coral",
        edgecolor="black",
    )
    plt.title("Distribuição de Idades dos Clientes")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade de clientes")
    plt.tight_layout()
    plt.show()


print("\n--- Visualização de Dados com Matplotlib ---")
print(f"Os dados são lidos de '{ARQUIVO_CSV}'.\n")

df = carregar_dados()

while True:
    print("\nMenu:")
    print("1 - Gráfico de barras: clientes por cidade")
    print("2 - Histograma: distribuição de idades")
    print("3 - Exibir ambos os gráficos")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        grafico_clientes_por_cidade(df)
    elif opcao == "2":
        histograma_idades(df)
    elif opcao == "3":
        grafico_clientes_por_cidade(df)
        histograma_idades(df)
    elif opcao == "4":
        print("\nEncerrando o programa.")
        break
    else:
        print("Opção inválida.")
