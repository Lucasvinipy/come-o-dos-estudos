print('cadastro completo')

dici={}
lista=[[],[],]
pessoas=0
soma=0
todas_as_pessoas=[]
while True:
    dici['nome']=input('nome: ')
    

    while True:
        sexo = input('Sexo (M/F): ').upper().strip()[0]
        if sexo == 'F' :
            dici['sexo'] = sexo
            pessoas=pessoas+1
            lista[0].append(dici['nome'])
            break
        if sexo == 'M':
            dici['sexo'] = sexo
            pessoas=pessoas+1
            break
        else:
            print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')
    dici['idade']=int(input('idade : '))
    soma=soma+dici['idade']

    print('='*50)

    todas_as_pessoas.append(dici.copy())

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

media=soma/pessoas

print(f'{pessoas} pessoas foram cadastradas')
print('<>'*50)
print(f'a media de idade é {media}')
print('==='*50)
print(f'as mulheres cadastradas foram{lista[0]}')
print('=='*50)

for pessoa in todas_as_pessoas:
    if pessoa['idade'] > media:
        lista[1].append([pessoa['idade'], pessoa['nome'], pessoa['sexo']])

print('Pessoas com idade acima da média:')
for pessoa in lista[1]:
    print(f'Idade = {pessoa[0]}, Nome = {pessoa[1]}, Sexo = {pessoa[2]}')
