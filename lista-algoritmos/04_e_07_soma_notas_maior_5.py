soma = 0
while True:
    nota = float(input('Digitie a nota (ou -1 para sair): '))
    if nota == -1:
        break
    if nota >= 5.0:
        soma += nota
        print(f'Soma das notas >= 5.0 {soma}')