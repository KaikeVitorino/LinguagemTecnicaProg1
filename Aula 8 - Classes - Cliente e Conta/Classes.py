class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def grava(c):
        f = open('cliente.txt', 'a')
        f.write(c.nome)
        f.write(c.sobrenome)
        f.write(c.cpf)
        f.close()

    def ler(c):
        f = open('cliente.txt', 'r')
        print('leitura de cliente')
        l = f.read()
        print(f"\n", l)

#====================================================#

class Conta:
    def __init__(self, nome, N_conta, saldo, limite):
        self.nome = nome
        self.N_conta = N_conta
        self.saldo = saldo
        self.limite = limite

    def grava(c):
        f = open('contas.txt', 'a')
        f.write(c.nome)
        f.write(c.N_conta)
        f.write(c.saldo)
        f.write(c.limite)
        f.close()

    def ler(c):
        f = open('contas.txt', 'r')
        print('leitura das contas')
        l = f.read()
        print(l)