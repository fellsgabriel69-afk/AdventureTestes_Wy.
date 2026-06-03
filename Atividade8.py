# Dicionário de Contatos
contatos = {}

while True:
    print("\n--- Dicionário de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        if not nome:
            print("Nome inválido.")
        elif nome in contatos:
            print(f"Já existe um contato com o nome '{nome}'.")
        else:
            telefone = input("Telefone: ").strip()
            email = input("E-mail: ").strip()
            contatos[nome] = {"telefone": telefone, "email": email}
            print(f"Contato '{nome}' adicionado com sucesso.")

    elif opcao == "2":
        nome = input("Digite o nome do contato: ").strip()
        if nome in contatos:
            contato = contatos[nome]
            print(f"\nNome: {nome}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            print("\nContatos cadastrados:")
            for nome, dados in contatos.items():
                print(f"\nNome: {nome}")
                print(f"Telefone: {dados['telefone']}")
                print(f"E-mail: {dados['email']}")

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
