#variaveis array
Nota = []
Aluno = []
# n = Numero de alunos
n = int(input("Qual a quantidade de alunos? "))

#Loop para ver qual a mencao da nota do aluno (A, B, C ou F)
for i in range(n):
    print('Aluno {}'.format(i+1))
    n1 = float(input('Digite a nota do Aluno: '))
    a1 = (input('Digite o nome do Aluno: '))
    #Coamndo append para add a nota e o nome nos arrays criados la em cima
    Nota.append(n1)
    Aluno.append(a1)

#printando os arrays ja completos com a notas e nomes do alunos
print('Notas: {}'.format(Nota))
print('Alunos: {}'.format(Aluno))

#Classificando nota dos alunos
for i in range(len(Nota)):
    if Nota[i] >=9.0:
        print('Conceito A para o aluno: ', Aluno[i])
    elif Nota[i] >= 8.0 and Nota[i] <= 8.9:
        print('Conceito B para o aluno: ', Aluno[i])
    elif Nota[i] >= 7.0 and Nota[i] <= 7.9:
        print('Conceito C para o aluno: ', Aluno[i])
    elif Nota[i] < 7.0:
        print('Conceito F para o aluno: ', Aluno[i])