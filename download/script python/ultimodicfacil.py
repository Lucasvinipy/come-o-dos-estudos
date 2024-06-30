import random 
import os 
os.system('cls')
lista=[[],[]]


def numeros(*noa):
    contador=0
    while contador < 5: 
        noa=random.randrange(1,10)
        contador=contador+1
        lista[0].append(noa)
    print(f'5 numeros aleatorios {lista[0]}')

def pares(*par):
    par=0
    for c in lista[0]:
        if c % 2 == 0:
            par=par+c
            lista[1].append(c)
    
    print(f'{lista[0]} a soma dos elementos {lista[1]} é : {par}')



numeros()
pares()
