import os
import time
os.system('cls')

print('progama que cadastra pessoas maior meso , meor peso , quantas pessoas')

guarda=[]
auxi=[]
maior=0
menor=400
while True:
    nome=input('nome : ')
    peso=float(input('peso : '))

    if peso > maior:
        maior=peso

    elif peso < menor:
        menor = peso

    



    auxi.append(peso)
    auxi.append(nome)

    guarda.append(auxi[:])

    auxi.clear

    wanted=input('continuar [S/N]').upper().strip()[0]

    if wanted not in "SN":
        print('opçao invalida')

    elif wanted == 'S':
        print('carregando')
        time.sleep(2)
        
    else:
        break


print(f'voce cadastrou {len(guarda)} pessoas')
print(f'a mais pesada {maior}')
print(f'a mais leve {menor}')
