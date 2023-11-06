import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data de abertura: ".format(self.data_abertura))
        print("Transacoes: ")
        for t in self.transacoes:
            print("-", t)

    def gravaHistorico(self):
        arq = open('historico.txt', 'a')
        arq.write()


class Cliente:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def gravar_cliente(self):
        arq_cli = open('Clientes', 'a')
        arq_cli.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f"|================================|\n")

    def ler_arq_cli(self):
        f = open('Clientes', 'r')
        print('|======| Leitura de cliente |======|')
        l = f.read()
        print(f"{l}\n")


class Conta(Cliente):
    def __init__(self, nome, cpf, n_conta, saldo):
        super().__init__(nome, cpf)
        self.n_conta = n_conta
        self.saldo = saldo
        self.historico = Historico()  # Crie uma instância de Historico

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(str(f"Depósito de {valor}. Saldo: {self.saldo}."))

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(str(f"Retirada de {valor}. Saldo: {self.saldo}."))
        else:
            print("Saldo insuficiente.")

    def transferencia_para(self, valor, destino):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.transacoes.append(str(f"Transferência de {valor} para conta {destino.n_conta}. Saldo: {self.saldo}."))
        else:
            print("Saldo insuficiente para a transferência.")


    def gravar_conta(self, nome, cpf):
        arq_cli = open('Contas', 'a')
        arq_cli.write(f"|================================|"
                      f"\n Nome: {nome}\n"
                      f" CPF: {cpf}\n"
                      f" Numero da conta: {self.n_conta}\n"
                      f" Saldo da conta: {self.saldo}\n")

    def ler_arq_conta(self):
        f = open('Contas', 'r')
        print('=====| Lista das contas |=====')
        l = f.read()
        print(f"\n", l)