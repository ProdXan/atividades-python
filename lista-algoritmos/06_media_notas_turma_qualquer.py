n = int(input('Quantidade de alunos: '))
soma = 0
for i in range(n):
    soma += float(input(f'Nota do aluno {i+1}: '))
    print(f'Média da turma: {soma/n:.2f}')
    