n = int(input('Quantos números? '))

numeros = []

for i in range(n):
    num = float(input("Digite um número: "))
    numeros.append(num)

    print('Maior:', max(numeros))
    print('Menor:', min(numeros))
    print('Média:', sum(numeros)/len(numeros))
    
