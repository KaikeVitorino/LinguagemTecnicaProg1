import random

def Menu():  # Func para mostrar o menu
    # Kake Vitorino 22301194
    # Victor Albuquerque 22309255
    # Gabriel Salustiano 22301008

    # Printa as opcoes
    print("\nEscolha umas das opcoes abaixo:\n"
          "2) Criar uma tupla de inteiros que vai retornar a soma, media menor e maior valor\n"
          "3) Recebe lista L e elimine os elementos repetidos\n"
          "4) Recebe 2 listas e retorna todos os elemtnos de L que nn estao na L2\n"
          "5) Recebe uma lista desordenada randomica, e retorna ela ordenada\n"
          "6) Func recursiva q retorna o produto dos elementos de uma lista de inteiros\n"
          "7) Criar um dicionario de N alunos com as respectivas notas\n"
          "8) Func que q retorna uniao de dois conjuntos\n"
          "9) Func que printa os retornos das func acima\n"#
          "1) <SAIR>\n")

    # Pergunta oq o usuario quer fazer
    escolha = input("Digite a opcao: ")
    while escolha not in ['2', '3', '4', '5', '6', '7', '8', '9']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")
    return escolha

def func02():
    #Vinicius Kenji Mizuno Inoue. RA:22308671
    #Guilherme Feydit. RA: 22251851
    tupla = (1, 3, 5, 6)

    if not tupla:
        return None

    soma = 0
    menor = tupla[0]
    maior = tupla[0]

    for elemento in tupla:
        soma += elemento

        if elemento < menor:
            menor = elemento

        if elemento > maior:
            maior = elemento

    media = soma / len(tupla)
    print(soma, media, menor, maior)
    return (soma, media, menor, maior)

def func03():
    # João Vitor Tomas Marra 22301440
    # Thiago Lucas Alves 22301651
    # Luiz Alberto Marques Lisot 22304614
    try:
        entrada = input("Digite a lista de números separados por espaços: ")
        lista = [int(numero) for numero in entrada.split()]
        lista_sem_repeticao = []

        for numero in lista:
            if numero not in lista_sem_repeticao:
                lista_sem_repeticao.append(numero)

        return print(lista_sem_repeticao)
    except ValueError:
        print("Erro: Certifique-se de que você inseriu números separados por espaços.")
        return None

def func04():
    def elementos_que_nao_estao_em_L2(L1, L2):
        # Ana Clara Alves da Silva/ RA:22304221 Luiz Eduardo/ RA:22305697
        return [elemento for elemento in L1 if elemento not in L2]

    lista1 = [1, 2, 3, 4, 5]
    lista2 = [3, 4, 5, 6, 7]
    resultado = elementos_que_nao_estao_em_L2(lista1, lista2)
    print(resultado)

def func05():
    '''
    5 funcao que ordena lista aleatoria

    Alex Hirth RA:22310283
    Bruno Rodrigues Barcelos RA:22302332
    '''
    x = random.sample(range(9), 9)

    print("lista aleatoria", x)

    # ordenando lista
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    print("lista ordenada:", x)

def func06():
    l = (1, 2, 3)     #Eles criaram umatulpa no lugar da lista, ent o codigo nn funciona como deveria

    # Gabriel Paiva - RA: 22301685
    # Lucas Andrade - RA: 22304505
    # Miguel Artur - RA: 22303780

    if type(l) != list:  # Se a não for uma lista, printa um erro e retorna <None>
        print(TypeError("Não é uma lista."))
        return

    if len(l) == 0:  # Se a lista for vazia retorna <1>

        return 1

    else:

        try:

            if type(l[0]) != int:  # Caso algum elemento não for <int> retorna um erro
                raise TypeError("Lista não é de inteiros.")

            return l[0] * func06(l[1:])  # Função recursiva

        except TypeError as e:

            print(e)  # printa erro e retorna <None>
            return

def func07():
# FUNÇÃO 7 - FELIPE AUGUSTO 22304569 ; MARCELLO MONTELLA 22300867 ; LÍVIA LEMOS 22300447

    alunos = {}
    i = 0

    while True:
        try:
            numeroDeAlunos = int(input('Quantos alunos para o dicionário? '))
            break
        except:
            print('Número de alunos tem que ser inteiro')


    while i < numeroDeAlunos:

        try:
            nome = input('Digite o nome do aluno ')
            nota = float(input('Digite a nota do aluno, de 0 a 10 '))
            if nota > 10 or nota < 0:
                raise TypeError('Nota inválida ')

            alunos.get(nome)
            alunos[nome] = nota

            i += 1

        except:
            print('Nota Inválida ')

    print(alunos)

    #A função 09 da print no return de todas as funções, se necessário pode remover esse print.

    return alunos

def func08():
    ## Nome: João Pedro Holanda da Costa / RA: 22309993
    ## Nome: Matheus Queiros / RA: 22309469
    def uniaoConjuntos(conjunto1, conjunto2):
        if not isinstance(conjunto1, set) or not isinstance(conjunto2, set):
            raise ValueError("Ambos têm que ser conjuntos.")

        return conjunto1 | conjunto2

    conjunto1 = set()
    conjunto2 = set()

    while True:
        elemento = input("Digite um elemento para o conjunto 1 (ou deixe em branco para parar): ")
        if not elemento:
            break
        conjunto1.add(elemento)

    while True:
        elemento = input("Digite um elemento para o conjunto 2 (ou deixe em branco para parar): ")
        if not elemento:
            break
        conjunto2.add(elemento)

    if not conjunto1 and not conjunto2:
        print("Aviso: Ambos os conjuntos estão vazios. A união também será um conjunto vazio.")
    else:
        uniao = uniaoConjuntos(conjunto1, conjunto2)
        print("União dos conjuntos:", uniao)

def func09():
    # Kaike Vitorino 22301194
    # Victor Albuquerque 22309255
    # Gabriel Salustiano 22301008
    print("função 2:\n")
    print(str(func02()), "\n")
    print("função 3:\n")
    print(str(func03()), "\n")
    print("função 4:\n")
    print(str(func04()), "\n")
    print("função 5:\n")
    print(str(func05()), "\n")
    print("função 6:\n")
    print(str(func06()), "\n")
    print("função 7:\n")
    print(str(func07()), "\n")
    print("função 8:\n")
    print(str(func08()))

#############################  MAIN  #############################

    # Kake Vitorino 22301194
    # Victor Albuquerque 22309255
    # Gabriel Salustiano 22301008

while True:
    escolha = Menu()  # Diz que a func Menu vai fornecer a escolha

    if escolha == '2':
        func02()

    elif escolha == '3':
        func03()

    elif escolha == '4':
        func04()

    elif escolha == '5':
        func05()

    elif escolha == '6':
        func06()
        pass

    elif escolha == '7':
        func07()
        pass

    elif escolha == '8':
        func08()
        pass

    elif escolha == '9':
        func09()

    elif escolha == '1':
        print("Saindo do programa...")
        break