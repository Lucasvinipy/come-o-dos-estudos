print('progama de gols')
soma = 0
dici = {}
lista = []
listagrande = []

while True:
    dici['nome'] = input('Nome do jogador: ')
    jogos = int(input('Quantos jogos ele jogou: '))

    for c in range(jogos):
        gols = int(input(f'Quantos gols na partida {c + 1}: '))
        lista.append(gols)

    dici['gols'] = lista.copy()  
    listagrande.append(dici.copy())  

    dici.clear()
    lista.clear()
    
    while True:
        continuar = input('Deseja cadastrar outra pessoa? (S/N): ').upper().strip()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            print('Por favor, digite S para sim ou N para não.')

    if continuar == 'N':
        break


print('*'*50)


for jogador in listagrande:
    print(f"Jogador: {jogador['nome']}")
    print(f"Gols por partida: {jogador['gols']}")


