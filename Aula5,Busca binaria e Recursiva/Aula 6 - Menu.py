def Menu():

    # Printa as opcoes
    print("Escolha umas das opcoes abaixo:\n"
          "a) Criar uma lista de inteiros e inserir N elementos\n"
          "b) Inverter a lista\n"
          "c) Retornar o produto dos elementos da lista\n"
          "d) Imprimir lista\n"
          "e) Criar um dicionario de N alunos com as respectivas notas\n"
          "f) Imprimir os launos om suas notas\n"
          "g) Alterar nota de um aluno do dicionario\n"
          "h) <SAIR>\n")

    # Pergunta oq o usuario quer fazer
    escolha = input("Digite a opcao: ")
    while escolha not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
    return escolha

def criar_lista(N, i=0, lista=None):
    if lista is None:
        lista = []
    if i == N:
        return lista
    elemento = int(input(f"Digite o elemento {i+1} da lista: "))
    lista.append(elemento)
    print("A lista foi criada.\n")
    return criar_lista(N, i+1, lista)

def inverter_lista(lista):
    lista.reverse()
    print("A lista foi invertida.\n")

def prod_da_lista(lista):
    produto = 1
    for elemento in lista:
        produto *= elemento
    print(f"O produto dos elementos da lista é: {produto}\n")
    return produto

while True:
    escolha = Menu()

    if escolha == 'a':
        N = int(input("Digite a quantidade de elementos da lista: "))
        lista = criar_lista(N)
    elif escolha == 'b':
        inverter_lista(lista)
    elif escolha == 'c':
        prod_da_lista(lista)
        pass
    elif escolha == 'd':
        print(f"Lista: {lista}\n")
    elif escolha == 'e':
        #  falta coisa
        pass
    elif escolha == 'f':
        #  falta coisa
        pass
    elif escolha == 'g':
        #  falta coisa
        pass
    elif escolha == 'h':
        print("Saindo do programa...")
        break