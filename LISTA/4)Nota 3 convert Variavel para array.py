#variaveis
Nota1 = float(input("Qual a nota do aluno1? "))
Aluno1 = (input("Qual nome do aluno1? "))

Nota2 = float(input("Qual a nota do aluno2? "))
Aluno2 = (input("Qual nome do aluno2? "))

Nota3 = float(input("Qual a nota do aluno3? "))
Aluno3 = (input("Qual nome do aluno3? "))

#Transfomando as variaveis acima em 2 arrays
Nota = [Nota1,Nota2,Nota3]
a = [Aluno1,Aluno2,Aluno3]

#Loop para ver qual o conceto da nota do aluno (A, B, C ou F)
for i in range(len(Nota)):
    if Nota[i] >=9.0:
        print('conceito A para o aluno: ', a[i])
    elif Nota[i] >= 8.0 and Nota[i] <= 8.9:
        print('conceito B para o aluno: ', a[i])
    elif Nota[i] >= 7.0 and Nota[i] <= 7.9:
        print('conceito C para o aluno: ', a[i])
    elif Nota[i] < 7.0:
        print('conceito F para o aluno: ', a[i])