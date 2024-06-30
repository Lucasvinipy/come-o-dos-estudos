print('progama analise de numeros')
num=(int(input('escolha os numeros:')),int(input('escolha os numeros:')),int(input('escolha os numeros:')),int(input('escolha os numeros:')))
print(f'voce digitou os numeros {num}')
if 3 in num:
    print(f'o valor 9 apareceu {num.count(9)} vezes')
else:
    print('o valor nao foi encontrado')
print(f'o valor 2 apareceu a primeira vez na posição{num.index(2) + 1}')
for p in num:
    if p % 2 == 0:
        print(f'{p} esses sao pares')
