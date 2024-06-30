import random
import os
os.system('cls')
print('\t jogo da adic=vinhação')
paplpites=0
lista=[1,2,3,4,5,6,7,8,9,10]
resultado=random.choice(lista)
tentativa=int(input('tente advinhar um numero entre 0 e 10:'))
while tentativa != resultado:
    
    if tentativa > resultado:
        print('voce errou..... o numero é menor')

    else:
        print('voce errou..... o numero é maior')
    
    tentativa=int(input('tente novamente:'))
    paplpites=paplpites  + 1

print('parabens voce acertou o {} e consegiu em {} palpites'.format(resultado,paplpites))