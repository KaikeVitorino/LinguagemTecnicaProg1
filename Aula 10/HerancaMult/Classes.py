'''
    Exemplo heranca multipla
'''

class Pessoa(object):
  # Classe base para pessoas.
  def __init__(self, idade, nome):
    self.idade = idade
    self.nome = nome

  def falar(self):
    print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Pai(Pessoa):
  # Classe para pais.

  def __init__(self, idade, nome, profissão):
    super().__init__(idade, nome)
    self.profissão = profissão

  def trabalhar(self):
    print(f"Olá, sou o {self.nome} e sou {self.profissão}.")


class Mãe(Pessoa):
  # Classe para mães.

  def __init__(self, idade, nome, filhos):
    super().__init__(idade, nome)
    self.filhos = filhos

  def cuidar_dos_filhos(self):
    print(f"Olá, sou a {self.nome} e estou cuidando dos meus filhos.")

class Filha(Pai, Mãe):
    # Classe para filhas.

  def __init__(self, idade, nome, profissão, filhos, hobbies):
    super().__init__(idade, nome, profissão)
    self.filha = filhos
    self.hobbies = hobbies

  def se_divertir(self):
    print(f"Olá, sou a {self.nome} e estou me divertindo com meus hobbies.")


# Exemplo de uso

filha = Filha(20, "Maria", "Estudante", [1, 2, 3], ["ler", "jogar", "dormir"])

filha.falar()
filha.trabalhar()
filha.cuidar_dos_filhos()
filha.se_divertir()
