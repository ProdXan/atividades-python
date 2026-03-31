contador = 0
while True:
    entrada = input('Idade do aluno (ou "fim"): ')
    if entrada.lower() == 'fim':
        break
    if int(entrada) == 30:
        contador += 1
        print(f'Quantidade de alunos com 30 anos: {contador}')
        