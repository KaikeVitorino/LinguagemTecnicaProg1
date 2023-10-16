class Fila:
    def __init__(self):
        self.fila = []

    def adicionar_elemento(self, elemento):
        self.fila.append(elemento)

    def printar_fila(self):
        print(self.fila)

    def remover_elemento(self):
        x = int(input("Escolhao indice: "))
        if len(self.fila) > 0:
            return self.fila.pop(x)
        else:
            print("A fila está vazia.")