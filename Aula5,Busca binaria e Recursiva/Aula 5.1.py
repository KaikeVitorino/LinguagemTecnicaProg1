#Recursiva = Func que puxa ela mesmo fazendo um loop diferenciado

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

l=[1,2,3]
resultado = soma_lista(l)
print(resultado)
