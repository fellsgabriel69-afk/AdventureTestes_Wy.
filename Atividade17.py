# Sistema Bancário (POO)


class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, valor):
        valor = float(valor)
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return False
        self.saldo += valor
        print(f"Depósito de R$ {valor:,.2f} realizado com sucesso.")
        return True

    def sacar(self, valor):
        valor = float(valor)
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {valor:,.2f} realizado com sucesso.")
        return True

    def verificar_saldo(self):
        return self.saldo

    def __str__(self):
        return (
            f"Conta {self.numero_conta} | Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:,.2f}"
        )


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

    def listar_contas(self):
        if not self.contas:
            print("Este cliente não possui contas cadastradas.")
            return
        print(f"\n--- Contas de {self.nome} ---")
        for conta in self.contas:
            print(conta)


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        for existente in self.clientes:
            if existente.cpf == cliente.cpf:
                print("Já existe um cliente cadastrado com este CPF.")
                return False
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso.")
        return True

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta(self, numero_conta):
        for cliente in self.clientes:
            conta = cliente.buscar_conta(numero_conta)
            if conta is not None:
                return conta
        return None

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return
        print(f"\n--- Clientes do {self.nome} ---")
        for indice, cliente in enumerate(self.clientes, start=1):
            print(f"{indice}. {cliente.nome} | CPF: {cliente.cpf} | Contas: {len(cliente.contas)}")


def normalizar_cpf(cpf):
    return "".join(c for c in str(cpf) if c.isdigit())


def cadastrar_cliente(banco):
    nome = input("Nome do cliente: ").strip()
    if not nome:
        print("O nome não pode estar vazio.")
        return

    cpf = normalizar_cpf(input("CPF: ").strip())
    if len(cpf) != 11:
        print("CPF inválido. Informe 11 dígitos.")
        return

    banco.adicionar_cliente(Cliente(nome, cpf))


def abrir_conta(banco):
    cpf = normalizar_cpf(input("CPF do cliente: ").strip())
    cliente = banco.buscar_cliente_por_cpf(cpf)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    try:
        numero_conta = input("Número da conta: ").strip()
        if not numero_conta:
            print("O número da conta não pode estar vazio.")
            return
        saldo_inicial = float(input("Saldo inicial (0 se não houver): ").strip().replace(",", ".") or 0)
    except ValueError:
        print("Saldo inicial inválido.")
        return

    if saldo_inicial < 0:
        print("O saldo inicial não pode ser negativo.")
        return

    if cliente.buscar_conta(numero_conta) is not None:
        print("Este cliente já possui uma conta com esse número.")
        return

    if banco.buscar_conta(numero_conta) is not None:
        print("Já existe uma conta com esse número no banco.")
        return

    conta = ContaBancaria(numero_conta, cliente.nome, saldo_inicial)
    cliente.adicionar_conta(conta)
    print(f"Conta {numero_conta} aberta para {cliente.nome}.")


def operar_conta(banco, operacao):
    numero_conta = input("Número da conta: ").strip()
    conta = banco.buscar_conta(numero_conta)
    if conta is None:
        print("Conta não encontrada.")
        return

    if operacao == "saldo":
        print(f"Saldo atual: R$ {conta.verificar_saldo():,.2f}")
        return

    try:
        valor = float(input("Valor: ").strip().replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return

    if operacao == "depositar":
        conta.depositar(valor)
    else:
        conta.sacar(valor)


def exibir_menu():
    print("\n--- Sistema Bancário ---")
    print("1. Cadastrar cliente")
    print("2. Abrir conta")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Verificar saldo")
    print("6. Listar clientes")
    print("7. Listar contas de um cliente")
    print("0. Sair")


def main():
    banco = Banco("Banco Wyden")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(banco)
        elif opcao == "2":
            abrir_conta(banco)
        elif opcao == "3":
            operar_conta(banco, "depositar")
        elif opcao == "4":
            operar_conta(banco, "sacar")
        elif opcao == "5":
            operar_conta(banco, "saldo")
        elif opcao == "6":
            banco.listar_clientes()
        elif opcao == "7":
            cpf = normalizar_cpf(input("CPF do cliente: ").strip())
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente is None:
                print("Cliente não encontrado.")
            else:
                cliente.listar_contas()
        elif opcao == "0":
            print("\nEncerrando o sistema bancário.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
