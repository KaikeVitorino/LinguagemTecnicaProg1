#Criando variveis
l = [3, 2, 1, 63, 64, 28, 100]
l1 = [1.34, 5.2]
w=l[0]
y=l[0]
i=t=0

#Criando loop para ver o maximo e o minimo com while
while i < len(l):
    x = l[i]
    print(x)
    if x > w:
        w = x
    if x < y:
        y = x
    i += 1
    t += x

# Printando geral
print("maior eh ", w)
print(max(l))
print("menor eh ", y)
print(min(l))
print("Total ", t)
print(t)