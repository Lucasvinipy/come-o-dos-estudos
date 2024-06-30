print('calculador de 0 a 500')
soma=0
cont=0
for c in range(1,501):
    if c % 2 == 0 and c % 3 == 0:
        soma=soma + 1
        cont = cont + c

print(cont,soma)