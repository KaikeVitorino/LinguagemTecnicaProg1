#Variavel
n = [9.5,9.5,7.5]
a = ['pedro','felipe','joaquim']

#For tipo de nota
for i in range(len(n)):
    if n[i] >=9.0:
        print('conceito A para o aluno: ', a[i])
    elif n[i] >= 8.0 and n[i] <= 8.9:
        print('conceito B para o aluno: ', a[i])
    elif n[i] >= 7.0 and n[i] <= 7.9:
        print('conceito C para o aluno: ', a[i])