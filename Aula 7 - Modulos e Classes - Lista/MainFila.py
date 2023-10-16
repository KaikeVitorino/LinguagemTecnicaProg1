from ClasseFila import *

def menu():
    f = Fila()

    while True:
        print("\nEscolha uma das opções abaixo:\n"
              "A) Adicionar elemento na fila\n"
              "B) Printar fila\n"
              "C) Tirar elemento da fila\n"
              "D) Sair")

        escolha = input("Digite a opção: ").lower()
        if escolha == 'a':
            elemento = input("Digite o elemento a ser adicionado na fila: ")
            f.adicionar_elemento(elemento)
        elif escolha == 'b':
            f.printar_fila()
        elif escolha == 'c':
            f.remover_elemento()
        elif escolha == 'd':
            break
        else:
            print("Opção inválida. Tente novamente.")

#=======================================   M   A   I   N   ============================================================#
menu()