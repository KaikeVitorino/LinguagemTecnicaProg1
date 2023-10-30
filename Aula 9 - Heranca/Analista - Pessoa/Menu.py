from Classes import *

def Menu(): # Func para mostrar o menu

    # Printa as opcoes
    print("\nEscolha umas das opcoes abaixo:\n"
          "A) Ler dados para gravar\n"
          "B) Imprimir dados arquivo\n"
          "C) Sair\n")

    # Pergunta oq o usuario quer fazer
    escolha = (input("Digite a opcao: ")).lower()

    while escolha not in ['a', 'b', 'c']:
        print("Opcao invalida. Tente novamente.\n")
        escolha = input("Digite a opcao: ")

    return escolha

def run():
    # Declarando variaveis para caso queria printar o arquivo sem adicionar pessoas novas
    nome = None
    idade = None
    linguagem = None
    nivel = None
    tempo_prof = None

    while True:
        escolha = Menu()

        if escolha == "a":
            nome = input("Qual o nome do usuario? ")
            idade = input("Qual a idade do usuario? ")
            linguagem = input("Qual a Linguagem de programacao usada pelo usuario? ")
            nivel = input("Qual o nivel de carreira do usuario? (Junior/Pleno/Senior): ")
            tempo_prof = input("Qual o tempo em anos de carreira do usuario? ")

            pessoa = Pessoa(nome, idade)
            analista = AnalistaSistemas(nome, idade, linguagem, nivel, tempo_prof)

            pessoa.gravar_pessoa_em_arquivo(nome, idade)
            analista.gravar_analista_em_arquivo(nome, idade, linguagem, nivel, tempo_prof)

        elif escolha == "b":

            pessoa = Pessoa(nome, idade)
            analista = AnalistaSistemas(nome, idade, linguagem, nivel, tempo_prof)

            pessoa.ler_pessoa()

            analista.ler_analista()

        else:
            print("Saindo...")
            break