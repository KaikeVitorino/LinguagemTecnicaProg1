from Classes import *

def menu():
    print(f"A) Adicionar cliente\n"
          f"B) Gravar cliente no arquivo\n"
          f"C) Ler arquivos de clientes\n"
          f"D) Adicionar conta do cliente\n"
          f"E) Gravar conta do cliente no arquivo\n"
          f"F) Ler arquivos de contas")

    escolha = input("\nDigite a opcao: ")
    escolha = escolha.lower()
    while escolha not in ['a', 'b', 'c', 'd', 'e', 'f']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
        escolha = escolha.lower()
    return escolha


# Declarando variaveis
nome_formatado = None
sobrenome_formatado = None
cpf_formatado = None
N_conta = None
saldo = None
limite = None

while True:
    escolha = menu()

    cliente = Cliente(nome_formatado, sobrenome_formatado, cpf_formatado)
    conta = Conta(nome_formatado, N_conta, saldo, limite)

    if escolha == "a":
        nome = input("Nome do cliente: ")
        nome_formatado = f"\nNome: {nome}"

        sobrenome = input("Sobrenome do cliente: ")
        sobrenome_formatado = f"Sobrenome: {sobrenome}\n"

        cpf = input("CPF do cliente: ")
        cpf_formatado = f"CPF: {cpf}"

    elif escolha == "b":
        if nome_formatado == None:
                print(f"\nVc nao tem um cliente para gravar!\n")

        else:
            cliente.grava()

    elif escolha == "c":
        cliente.ler()

    elif escolha == "d":
        if nome_formatado == None:
            print("Vc nn tem um cliente para adicionar uma conta!")

        else:
            N_conta = input("Numero da conta do cliente: ")
            N_conta = f"\nNumero da conta: {N_conta}\n"

            saldo = input("Quantidade de saldo do cliente: ")
            saldo = f"Saldo: {saldo}\n"

            limite = input("Limite do cliente: ")
            limite = f"Limite: {limite}\n"

            conta = Conta(nome_formatado, N_conta, saldo, limite)

    elif escolha == "e":
            conta.grava()

    elif escolha == "f":
            conta.ler()

#=======================================