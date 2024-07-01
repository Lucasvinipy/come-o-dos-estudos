import random
import os
import time

os.system('cls')

lista = []
jogos = []
print('-' * 30)
print(' ' * 6, 'JOGA NA MEGA SENA', ' ' * 6)
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    time.sleep(2)
print(f'{quant} jogadas geradas BOA SORTE!!!!!!!!!! ')