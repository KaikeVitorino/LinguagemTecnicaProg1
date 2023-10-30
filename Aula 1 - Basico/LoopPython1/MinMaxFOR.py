#Criando variveis
l = [3, 2, 1, 63, 64, 28, 100]
l1 = [1.34, 5.2]
w=l[0]
y=l[0]
i=t=0

#Criando loop para ver o maximo e o minimo
print("Primeira iteracao do for in")
for x in l:
    print(x)
    if l[i]>w:
        w=l[i]
    if l[i] < y:
      y = l[i]
    i=i+1
    t = t+x

#Printando geral
print("maior eh ", w)
print(max(l))
print("menor eh ", y)
print(min(l))
print("Total ", t)
print(t)
