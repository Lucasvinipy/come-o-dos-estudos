print('progama de gols')

dici={}
lista=[]
while True:
    dici['nome']=input('nome jogador : ')
    jogos=int(input('quantos jogos ele jogou : '))

    for c in range(jogos):
        gols=int(input(f'quantos gols na partida {c+1} : '))
        lista.append(gols)

    dici['gols']=lista
    
    dici['total']=sum(lista)

    break

print('='*50)

print(dici)

print('='*50)

for c , v in dici.items():
    print(f'{c} tem o valor {v}')

print('='*50)

print(f'o jogador {dici['nome']} jogou {jogos:<5}')
for c in range(jogos):
    print(f'\t na partida {c+1} , fez {dici["gols"][c]} ')
    
print('='*50)

print(f'foi um total de {dici['total']} gols ')