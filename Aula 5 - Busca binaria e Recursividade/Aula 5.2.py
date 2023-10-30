#Target eh oq vc quer achar na lista
#Array eh a lista em q vc quer achar um elemento
#Menor = Limite minimo = 0
#Maior = limite maximo = len(array) - 1  (-1 pq em python o indice comeca do 0)
#Meio = indice do Meio da lista
#Logica do jogo de descobrir numero, ele chuta o numero do meio
#Se o numero do meio for o correto ele para e retorna o numero do indice
#Se o numero meio for maior ent ele atualiza o numero maximo para o indice menos 1
#E vai dividindo a lista por 2 assim aumentando a produtividade

def pesquisa_bin(array, target):
    Menor = 0
    Maior = len(array) - 1
    while Menor <= Maior:
        Meio = (Menor + Maior) // 2
        if array[Meio] == target:
            return Meio
        elif array[Meio] < target:
            Menor = Meio + 1
        else:
            Maior = Meio - 1
    return -1

L=range(123, 237)
X = int(input("Qual o numero q vc quer: "))
Index_Target = pesquisa_bin(L, X)
print("Indice do target: ", Index_Target)
