class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def gravar_pessoa_em_arquivo(self, nome, idade):
        with open("!Pessoa_em_arquivo", "a") as arquivo:
            arquivo.write(f"Nome: {nome}")
            arquivo.write(f"\nIdade: {idade} anos\n")
            arquivo.write(f"\n")

    def ler_pessoa(self):
        f = open('!Pessoa_em_arquivo', 'r')
        print('\n============ Leitura de Pessoas ============\n')
        l = f.read()
        print(l)
        print("|=============================================|\n")

class AnalistaSistemas(Pessoa):
    def __init__(self, nome, idade, linguagem, nivel, tempo_prof):
        super().__init__(nome, idade)
        self.linguagem = linguagem
        self.nivel = nivel
        self.tempo_de_profissao = tempo_prof

    def gravar_analista_em_arquivo(self, nome, idade, linguagem, nivel, tempo_prof):
        with open("!Analista_em_arquivo", "a") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Idade: {idade} anos\n")
            arquivo.write(f"Linguagem de programacao: {linguagem}\n")
            arquivo.write(f"Nivel de carreira: {nivel}\n")
            arquivo.write(f"Tempo de profissao: {tempo_prof}\n")
            arquivo.write(f"\n")

    def ler_analista(self):
        f = open('!Analista_em_arquivo', 'r')
        print('|============ Leitura de Analista ============|\n')
        l = f.read()
        print(l)
        print("|=============================================|")