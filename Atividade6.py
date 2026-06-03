# Lista de Compras
lista_compras = []

while True:
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Retirar item da lista")
    print("3 - Visualizar itens")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a adicionar: ").strip()
        if item:
            lista_compras.append(item)
            print(f"'{item}' adicionado à lista.")
        else:
            print("Item inválido.")

    elif opcao == "2":
        if not lista_compras:
            print("A lista está vazia.")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i} - {item}")
            try:
                indice = int(input("Digite o número do item a retirar: ")) - 1
                if 0 <= indice < len(lista_compras):
                    removido = lista_compras.pop(indice)
                    print(f"'{removido}' retirado da lista.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

    elif opcao == "3":
        if not lista_compras:
            print("A lista está vazia.")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i} - {item}")

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
