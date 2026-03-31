soma = 0
cont = 0
while True:
    entrada = input("Nota (ou 'encerrar'): ")
    if entrada.lower() == 'encerrar':
        break
    nota = float(entrada)
    if 5.0 < nota < 7.0:
        soma += nota
        cont += 1
    if cont > 0:
        print(f'Média das notas entre 5 e 7: {soma/cont:.2f}')
        