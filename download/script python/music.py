from random import randint
from time import sleep 
escolha = randint(0,5)
print('vou pensar em um numero de 0 a 5 ')
tentativa=int(input('em que numero pensei:'))
sleep(5)
if tentativa == escolha:
    print('parabens voce acertou')
else:
    print('voce errou o numero que eu pensei foi {}'.format(escolha))