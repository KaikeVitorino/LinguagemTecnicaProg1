def Menu(): # Func para mostrar o menu

    # Printa as opcoes
    print("\nEscolha umas das opcoes abaixo:\n"
          "a) Criar uma lista de inteiros e inserir N elementos\n"
          "b) Inverter a lista\n"
          "c) Retornar o produto dos elementos da lista\n"
          "d) Imprimir lista\n"
          "e) Criar um dicionario de N alunos com as respectivas notas\n"
          "f) Imprimir os alunos com suas notas\n"
          "g) Alterar nota de um aluno do dicionario\n"
          "h) <SAIR>\n")

    # Pergunta oq o usuario quer fazer
    escolha = input("Digite a opcao: ")
    while escolha not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
    return escolha

def criar_lista(N, i=0, lista=None): # Func para criar lista
    if lista is None:
        lista = []
    while i < N:
        try:
            elemento = int(input(f"Digite o elemento {i+1} da lista: "))
            lista.append(elemento)
            i += 1
        except ValueError:
            print("Erro: Insira um número inteiro")
            escolha = input("Digite 'M' para voltar ao menu ou 'S' para sair: ").lower()
            if escolha == 's':
                return None  # Retorna None porque a lista nao foi criada
    return lista

def inverter_lista(lista): # Func para inverter a lista
    try:
        lista.reverse()
        print("A lista foi invertida.")
    except AttributeError:
        print("Erro: Vc precisa criar uma lista primeiro.")
        escolha = input("Digite 'M' para voltar ao menu ou 'S' para sair: ").lower()
        if escolha == 's':
            return  # Sai da função, não inverte a lista

def produto_da_lista(lista): # Func para mostrar a multiplicacao da lista
    try:
        produto = 1
        for elemento in lista:
            produto *= elemento
        print(f"O produto dos elementos da lista é: {produto}")
    except TypeError:
        print("Erro: Vc precisa criar uma lista primeiro.")
        escolha = input("Digite 'M' para voltar ao menu ou 'S' para sair: ").lower()
        if escolha == 's':
            return

def Criar_Dic_Alunos(N): # Cria dicionario de alunos
    Info_Alunos = {}
    for i in range(N):
        try:
            nome_aluno = input(f"Digite o nome do aluno {i+1}: ")
            nota = float(input(f"Digite a nota do aluno {nome_aluno}: "))
            Info_Alunos[nome_aluno] = nota
        except ValueError:
            print("Erro: Insira um valor numérico válido para a nota.")
    return Info_Alunos

def imprimir_dic_alunos(dic_alunos): # Imprime o dicionario dos alunos
    if dic_alunos is None:
        print("Erro: Você precisa criar um dicionário de alunos primeiro.")
        return

    for aluno, nota in dic_alunos.items():
        print(f"Aluno: {aluno}, Nota: {nota}")


def alterar_nota_aluno(dic_alunos):
    if dic_alunos is None:
        print("Erro: Você precisa criar um dicionário de alunos primeiro.")
        return

    imprimir_dic_alunos(dic_alunos)

    try:
        escolha_aluno = int(input("Selecione o número do aluno que deseja alterar a nota: "))

        if 1 <= escolha_aluno <= len(dic_alunos):
            alunos = list(dic_alunos.keys())
            nome_aluno = alunos[escolha_aluno - 1]

            nova_nota = float(input(f"Digite a nova nota para {nome_aluno}: "))
            dic_alunos[nome_aluno] = nova_nota
            print(f"A nota de {nome_aluno} foi atualizada para {nova_nota}.")
        else:
            print("Escolha inválida. Selecione um número válido de aluno.")
    except ValueError:
        print("Erro: Insira um número válido.")

#===============================  Main para rodar tudo  ===============================#
while True:
    escolha = Menu()  # Diz que a func Menu vai fornecer a escolha

    if escolha == 'a':
        while True:
            N = input("Digite a quantidade de elementos da lista: ")
            if N.isdigit():
                N = int(N)
                lista = criar_lista(N)
                break
            else:
                print("Erro: N não é um número inteiro. Tente novamente.")

    elif escolha == 'b':
        inverter_lista(lista)

    elif escolha == 'c':
        prod_da_lista(lista)

    elif escolha == 'd':
        if 'lista' in locals():
            print(f"Lista: {lista}")
        else:
            print("Erro: Você precisa criar uma lista primeiro.")

    elif escolha == 'e':
        while True:
            N = input("Digite a quantidade de alunos: ")
            if N.isdigit():
                N = int(N)
                Info_Alunos = Criar_Dic_Alunos(N)
                break
            else:
                print("Erro: N não é um número inteiro. Tente novamente.")

    elif escolha == 'f':
        imprimir_dic_alunos(Info_Alunos)
        pass

    elif escolha == 'g':
        alterar_nota_aluno(Info_Alunos)
        pass

    elif escolha == 'h':
        print("Saindo do programa...")
        break