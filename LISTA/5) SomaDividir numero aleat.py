#import da funcao que pode geral numeros aleatorios
from random import randint

#Criando lista de aleatorios com [] pq eh um array
lr=[]
#Criando variaveis inteiras
#n = numero de vezes q ele vai gera o numero aleatorio e soma-lo
n = int(input("Digite N: "))
total = 0
i = 1

# While loop para somar os valores gerados pela funcao de numero aleatorios
# Simbolo para por numero dentro do print randint {}
while i<= n:
    x = randint(1, 50)
    #lr.append adiciona os numero aleatorios ao array
    lr.append(x)
    print("Valor {} valor gerado {}"
        .format(i,x))
    total = total + x
    i += 1
    #printando a resposta e o array com a lista de numero aleatorios gerados
    print('\n', lr)
    print("\nSoma dos valores gerados = {}"
        .format(total))

