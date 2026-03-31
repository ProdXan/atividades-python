soma = 0
cont = 0
while True:
    entrada = input("Idade (ou 'parar'): ")
    if entrada.lower() == 'parar':
        break
    idade = int(entrada)
    if 25 < idade < 40:
     soma += idade
    cont += 1
    if cont > 0:
        print(f"Média das idades entre 25 e 40: {soma/cont:.2f}")
    else:
        print("Nenhum aluno nesta faixa etária.")
