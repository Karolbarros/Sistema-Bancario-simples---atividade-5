class Conta_bancaria:
    def __init__(self, titular, cpf):
        self.titular = titular
        self.cpf = cpf
        self.saldo = 0.0

    def mostrar_conta(self):
        return (f'Titular: {self.titular}, CPF: {self.cpf}, Saldo: R$ {self.saldo:.2f}')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Saque inválido. Verifique o valor e seu saldo.')

    def verificar_saldo(self):
        return f'Saldo atual: R$ {self.saldo:.2f}'


class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, numerocc):
        super().__init__(titular, cpf)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f'Conta Corrente - {self.mostrar_conta()}, Número da Conta: {self.numerocc}'


class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, rendimento):
        super().__init__(titular, cpf)
        self.rendimento = rendimento

    def ver_rendimento(self):
        return f'Taxa de Rendimento: {self.rendimento * 100:.2f}%'

    def render(self):
        rendimento_calculado = self.saldo * self.rendimento
        self.saldo += rendimento_calculado
        print(f'Rendimento de R$ {rendimento_calculado:.2f} aplicado com sucesso!')


def menu():
    contas = []
    
    while True:
        print("\n--- Menu do Banco ---")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Poupança")
        print("3. Depositar em Conta")
        print("4. Sacar de Conta")
        print("5. Verificar Saldo de Conta")
        print("6. Ver Rendimento (Poupança)")
        print("7. Aplicar Rendimento (Poupança)")
        print("8. Mostrar Lista de Contas")
        print("9. Sair")
        
        opcao = input("Escolha uma opção (1-9): ")
        
        if opcao == '1':
            titular = input("Digite o nome do titular: ")
            cpf = input("Digite o CPF do titular: ")
            numerocc = input("Digite o número da conta corrente: ")
            conta = Conta_corrente(titular, cpf, numerocc)
            contas.append(conta)
            print("Conta Corrente criada com sucesso!")
        
        elif opcao == '2':
            titular = input("Digite o nome do titular: ")
            cpf = input("Digite o CPF do titular: ")
            rendimento = float(input("Digite a taxa de rendimento (em decimal): "))
            conta = Conta_poupanca(titular, cpf, rendimento)
            contas.append(conta)
            print("Conta Poupança criada com sucesso!")
        
        elif opcao == '3':
            if not contas:
                print("Nenhuma conta disponível. Crie uma conta primeiro.")
                continue
            for i, conta in enumerate(contas):
                print(f"{i + 1}. {conta.mostrar_conta()}")
            escolha = int(input("Escolha a conta para depositar: ")) - 1
            valor = float(input("Digite o valor a ser depositado: "))
            contas[escolha].depositar(valor)
        
        elif opcao == '4':
            if not contas:
                print("Nenhuma conta disponível. Crie uma conta primeiro.")
                continue
            for i, conta in enumerate(contas):
                print(f"{i + 1}. {conta.mostrar_conta()}")
            escolha = int(input("Escolha a conta para sacar: ")) - 1
            valor = float(input("Digite o valor a ser sacado: "))
            contas[escolha].sacar(valor)
        
        elif opcao == '5':
            if not contas:
                print("Nenhuma conta disponível. Crie uma conta primeiro.")
                continue
            for conta in contas:
                print(conta.verificar_saldo())
        
        elif opcao == '6':
            if not contas:
                print("Nenhuma conta disponível. Crie uma conta primeiro.")
                continue
            for i, conta in enumerate(contas):
                if isinstance(conta, Conta_poupanca):
                    print(f"{i + 1}. {conta.ver_rendimento()}")
        
        elif opcao == '7':
            if not contas:
                print("Nenhuma conta disponível. Crie uma conta primeiro.")
                continue
            for i, conta in enumerate(contas):
                if isinstance(conta, Conta_poupanca):
                    print(f"{i + 1}. {conta.mostrar_conta()}")
            escolha = int(input("Escolha a conta poupança para aplicar rendimento: ")) - 1
            contas[escolha].render()
        
        elif opcao == '8':
            if not contas:
                print("Nenhuma conta disponivel.")
            else:
                print("\n--- Lista de Contas ---")
                for i, conta in enumerate(contas):
                    if isinstance(conta, Conta_corrente):
                        print(f"{i + 1}. {conta.mostrarcc()}")
                    elif isinstance(conta, Conta_poupanca):
                        print(f"{i + 1}. {conta.mostrar_conta()} - Tipo: Poupança")
        
        elif opcao == '9':
            print("Saindo do sistema. Ate mais!")
            break
        
        else:
            print("Opção inválida!!!! Tente novamente.")


menu()
