alunos = {}

while True:
    nome = input('Nome: ')
    media = float(input(f'Média de {nome}: '))

    if media >= 5:
        situacao = 'aprovado'
    elif media < 3:
        situacao = 'reprovado'
    else:
        situacao = 'exame'

    alunos[nome] = {'media': media, 'situação': situacao}

    continuar = input('Continuar [S/N]: ').upper().strip()[0]
    
    while continuar not in 'SN':
        print('Opção inválida. Tente novamente...')
        continuar = input('Continuar [S/N]: ').upper().strip()[0]

    if continuar == 'N':
        break

print('=' * 50)

for nome, dados in alunos.items():
    print(f'Nome: {nome}, Média: {dados["media"]}, Situação: {dados["situação"]}')
