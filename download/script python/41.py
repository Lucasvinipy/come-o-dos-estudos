print('progama que le numeros interios')
soma=0
for c in range(6):
    num=int(input('digite o numero'))
    if num % 2 == 0:
        soma=soma+num
    else:
        num=0
print(soma)