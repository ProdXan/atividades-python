soma = 0
for i in range(1, 31):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    soma += idade
    print(f"A soma das idades é: {soma}")