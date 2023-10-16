from Calcula import *

def menu_calculadora():
    print("\nEscolha umas das opcoes abaixo:\n"
          "A) Numeros para primeira operacao\n"
          "B) +\n"
          "C) -\n"
          "D) ×\n"
          "E) ÷\n")

    # Pergunta oq o usuario quer fazer
    escolha = input("Digite a opcao: ")
    while escolha not in ['a', 'b', 'c', 'd', 'e']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
    return escolha

def calculadora():
    c = Calcula()
    while True:
        escolha = menu_calculadora()  # Diz que a func Menu vai fornecer a escolha

        if escolha == 'a':
            lista_numeros = Decidir_Numero()

        elif escolha == 'b':
            print(c.soma(lista_numeros))

        elif escolha == 'c':
            print(c.subtrair(lista_numeros))

        elif escolha == 'd':
            print(c.multiplicar(lista_numeros))

        elif escolha == 'e':
            print(c.dividir(lista_numeros))

            break


