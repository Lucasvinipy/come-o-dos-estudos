print('Programa de Sexo e Idade')

lista = []

mulheres = 0
soma35 = 0
quantidade = 0

for c in range(4):
    while True:
        sexo = input('Sexo (M/F): ').upper().strip()[0]
        if sexo in 'MF':
            lista.append(sexo)
            if sexo == 'F':
                mulheres += 1
            break
        else:
            print('Sexo inválido. Por favor, insira "M" ou "F".')

    idade = int(input('Idade: '))
    lista.append(idade)

    if idade > 35 and sexo == 'M':
        quantidade += 1
        soma35 += idade

if quantidade > 0:
    media = soma35 / quantidade
else:
    media = 0

print(f'Média das idades dos homens com mais de 35 anos: {media}')
print(f'Lista completa: *{lista}')
print(f'Quantidade de mulheres: {mulheres}')
