import os
os.system('cls')

print('\t progama de genero')
genero=input('escolha seu genero   M/F :').strip().upper()[0]
while genero != 'M' and genero != 'F':
    print(' genero invalido \n pressione enter para ir novamante')
    genero=input('escolha seu genero:').strip().upper()[0]
print('genero {} registrado com sucesso'.format(genero))
    