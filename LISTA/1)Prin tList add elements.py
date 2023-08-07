#Dada essa lista abaixo:
L = [5, 4, 3, 2, 8, 7, 4,9]

#1. IMPRIMA OS 3 ULTIMOS ELEMENTOS

print(L[5:])

#2. ORDENE A LISTA CRESCENTE E DECRESCENTE
# L.sort = Crescente // L.reverse = Decrescente

L.sort(reverse=True)
print(L)

L.sort()
print(L)

#3. INSIRA UM ELEMENTO NO INICIO DA L

L.insert(0, 452)
print(L)

#4. Print tipo

print(type(L))