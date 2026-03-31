soma = 0
for i in range(1, 51):
    idade = int(input(f"Digite a idade do aluno {i}"))
    soma += idade
media = soma / 50
print(f'A média das idades é: {media:.2f}')
