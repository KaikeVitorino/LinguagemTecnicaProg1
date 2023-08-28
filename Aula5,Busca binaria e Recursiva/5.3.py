def soma(*valores):
    s = 0
    print(type(valores))
    for i in range(len(valores)):
        s = s + valores[i]

    return s

print(soma(1,2,3))

#-----------------------------------------#

def soma2(x,y,z):

    return (x+y+z)

t = (1, 2, 3)
print(soma2(*t))