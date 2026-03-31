num = int(input("Verificar se o número é primo: "))
mult = 0
for count in range(2,num):
    if num % count == 0:
        mult += 1

if mult == 0 and num > 1:
    print("É primo")
else:
    print("Não é primo")
    
