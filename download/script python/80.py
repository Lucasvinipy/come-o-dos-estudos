import os 
import random 
import time

os.system('cls')  


resultados = {}


for c in range(4):
    num = random.randint(1, 6)
    jogador = f'jogador {c + 1}'
    resultados[jogador] = num 
    print(f'O {jogador} obteve {num}')
    time.sleep(1)

print('='*50)

ranking = sorted(resultados.items(), key=lambda item: item[1], reverse=True)

print('-'*2, 'RANKING DOS JOGADORES', '-'*2)
for posicao, (jogador, resultado) in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador} com {resultado}')


print('\nResultados:', resultados)
