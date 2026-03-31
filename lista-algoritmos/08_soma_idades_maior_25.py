soma = 0
while True:
    entrada = input('Idade (ou "sair"): ')
    if entrada.lower() == 'sair':
        break
    idade = int(entrada)
    if idade > 25:
        soma += idade
        print(f'Soma das idades > 25: {soma}')
