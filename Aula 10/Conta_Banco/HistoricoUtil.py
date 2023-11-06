import datetime

class historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data de abertura: {}".format(self.data_abertura))
        print("Transacoes: ")
        for t in self.transacoes:
            print("-", t)

    def gravaHistorico(self):
        arq = open('historico.txt', 'a')
        arq.write()


class cliente:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def gravar_cliente(self):
        arq_cli = open('Clientes', 'a')
        arq_cli.write(f"\nNome: {self.nome}"
                      f"CPF: {self.cpf}\n")

    def ler_arq_cli(self):
        f = open('Clientes', 'r')
        print('=====| Leitura de cliente |=====')
        l = f.read()
        print(f"\n", l)


class conta(cliente):
    def __init__(self, nome, cpf, n_conta, saldo):
        super().__init__(nome, cpf)
        self.n_conta = n_conta
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Deposito de {} ".format(self.saldo))

    def saca(self, valor):
        self.saldo -= valor
        self.historico.transacoes.append("Retirada de {}".format(self.saldo))

    def transferencia_para(self, valor, destino):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia de {} para conta {}".format(self.saldo))
