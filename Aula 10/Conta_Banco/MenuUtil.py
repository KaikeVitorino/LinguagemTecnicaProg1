from HistoricoUtil import * # Importando o modulo das classes criadas por mim
import random # Importando o modulo random para gerar o numero da conta dos clientes

# Criando funcao do Menu
def menu():
    print(f"A) Adicionar cliente\n"
          f"B) Ver infos dos clientes\n"
          f"C) Ver infos das contas dos clientes\n"
          f"D) Depositar\n"
          f"E) Sacar\n"
          f"F) Transferir\n"
          f"G) Ver historico de movimentacao da conta\n"
          f"H) Salvar historico de movimentacao\n"
          f"I) Sair do Programa")

    escolha = input("\nDigite a opcao: ")
    escolha = escolha.lower()

    while escolha not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
        escolha = escolha.lower()
    return escolha

def main():

    #Declarando variaveis essenciais
    nome = None
    cpf = None
    saldo = None
    n_conta = random.randint(0, 100000000)

    cliente = Cliente(nome, cpf)
    conta = Conta(Cliente, Historico, n_conta, saldo)
    historico = Historico()

    while True:
        escolha = menu()

        if escolha == 'a':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            saldo = input("Saldo disponivel na conta do cliente: ")
            print(f"Numero da conta do cliente: {n_conta} \n")

            cliente = Cliente(nome, cpf)
            conta = Conta(Cliente, Historico, n_conta, saldo)

            cliente.gravar_cliente()
            conta.gravar_conta(nome, cpf)

        elif escolha == 'b':
            cliente.ler_arq_cli()

        elif escolha == 'c':
            conta.ler_arq_conta()

        elif escolha == 'd':
            valor = input("Valor a ser depositado: ")
            conta.deposita(valor)

        elif escolha == 'e':
            valor = input("Valor a ser sacado: ")
            conta.saca(valor)

        elif escolha == 'f':
            destino = input("Pessoa destino da transferencia: ")
            valor = input("Valor a ser transferido: ")

            conta.transferencia_para(valor, destino)

        elif escolha == 'g':
            historico.imprime()

        elif escolha == 'h':
            historico.gravaHistorico()

        else:
            print("Encerrando programa...")
            break