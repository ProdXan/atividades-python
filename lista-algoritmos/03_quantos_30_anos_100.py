contador = 0
for i in range(1, 101):
    idade = int(input(f'Idade do aluno {i}: '))
    if idade == 30:
        contador += 1
print(f'Total de alunos com 30 anos: {contador}')
