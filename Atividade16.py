# Análise de Dados com Pandas
import os

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


def salvar_dados(df):
    df.to_csv(ARQUIVO_CSV, index=False, encoding="utf-8")


def adicionar_cliente(df):
    nome = input("Nome: ").strip()
    if not nome:
        print("O nome não pode estar vazio.")
        return df

    cidade = input("Cidade: ").strip()
    if not cidade:
        print("A cidade não pode estar vazia.")
        return df

    try:
        idade = int(input("Idade: ").strip())
        renda = float(input("Renda: ").strip().replace(",", "."))
    except ValueError:
        print("Idade e renda devem ser números válidos.")
        return df

    if idade <= 0 or renda < 0:
        print("A idade deve ser maior que zero e a renda não pode ser negativa.")
        return df

    novo = pd.DataFrame(
        [{"Nome": nome, "Idade": idade, "Cidade": cidade, "Renda": renda}]
    )
    df = pd.concat([df, novo], ignore_index=True)
    salvar_dados(df)
    print("Cliente cadastrado com sucesso.")
    return df


def calcular_medias(df):
    if df.empty:
        return None, None
    return df["Idade"].mean(), df["Renda"].mean()


def cidade_com_mais_clientes(df):
    if df.empty:
        return None, 0
    contagem = df["Cidade"].value_counts()
    return contagem.index[0], int(contagem.iloc[0])


def filtrar_por_renda(df, renda_minima):
    return df[df["Renda"] > renda_minima]


def listar_clientes(df):
    if df.empty:
        print("\nNenhum cliente cadastrado.")
        return

    print("\n--- Clientes ---")
    for indice, (_, linha) in enumerate(df.iterrows(), start=1):
        print(
            f"{indice}. {linha['Nome']} | "
            f"{int(linha['Idade'])} anos | "
            f"{linha['Cidade']} | "
            f"R$ {linha['Renda']:,.2f}"
        )


def exibir_resumo(df):
    if df.empty:
        print("\nNenhum cliente cadastrado para análise.")
        return

    media_idade, media_renda = calcular_medias(df)
    cidade, total = cidade_com_mais_clientes(df)

    print("\n--- Resumo da análise ---")
    print(f"Total de clientes: {len(df)}")
    print(f"Média de idade: {media_idade:.1f} anos")
    print(f"Média de renda: R$ {media_renda:,.2f}")
    print(f"Cidade com mais clientes: {cidade} ({total} clientes)")


print("\n--- Análise de Dados com Pandas ---")
print(f"Os dados são salvos em '{ARQUIVO_CSV}'.\n")

df = carregar_dados()

while True:
    print("\nMenu:")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Exibir médias de idade e renda")
    print("4 - Cidade com mais clientes")
    print("5 - Filtrar clientes por renda mínima")
    print("6 - Exibir resumo completo")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        df = adicionar_cliente(df)
    elif opcao == "2":
        listar_clientes(df)
    elif opcao == "3":
        media_idade, media_renda = calcular_medias(df)
        if media_idade is None:
            print("\nNenhum cliente cadastrado.")
        else:
            print(f"\nMédia de idade: {media_idade:.1f} anos")
            print(f"Média de renda: R$ {media_renda:,.2f}")
    elif opcao == "4":
        cidade, total = cidade_com_mais_clientes(df)
        if cidade is None:
            print("\nNenhum cliente cadastrado.")
        else:
            print(f"\nCidade com mais clientes: {cidade} ({total} clientes)")
    elif opcao == "5":
        try:
            renda_minima = float(
                input("Informe a renda mínima: ").strip().replace(",", ".")
            )
        except ValueError:
            print("Informe um valor numérico válido.")
            continue

        filtrados = filtrar_por_renda(df, renda_minima)
        print(f"\nClientes com renda acima de R$ {renda_minima:,.2f}:")
        listar_clientes(filtrados)
    elif opcao == "6":
        exibir_resumo(df)
    elif opcao == "7":
        print("\nEncerrando o programa.")
        break
    else:
        print("Opção inválida.")
