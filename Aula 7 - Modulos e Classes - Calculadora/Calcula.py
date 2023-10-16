class Calcula():

    def soma(self, lista_numeros):
        return sum(lista_numeros)

    def subtrair(self, lista_numeros):
        return lista_numeros[0] - sum(lista_numeros[1:])

    def multiplicar(self, lista_numeros):
        resultado = 1
        for num in lista_numeros:
            resultado *= num
        return resultado

    def dividir(self, lista_numeros):
        try:
            resultado = lista_numeros[0]
            for num in lista_numeros[1:]:
                resultado /= num
            return resultado
        except ZeroDivisionError:
            return "Erro: Divisão por zero não é permitida"


def Decidir_Numero():
    N = int(input("Digite a quantidade de numeros: \n"))
    lista_numeros = []
    for i in range(N):
        try:
            Numero = float(input(f"Digite o {i + 1}º numero: "))
            lista_numeros.append(Numero)
        except ValueError:
            Numero = float(0)
            lista_numeros.append(Numero)
            print("Isso nn eh um valor numérico válido. Numero 0 considerado.")

    print(lista_numeros)
    print("Escolha agora no menu a operacao matematia a ser realizada: \n")
    return lista_numeros
