print('Cadastro completo')

while True:
    dici = {}
    
    dici['nome'] = input('Nome: ')
    
    while True:
        sexo = input('Sexo (M/F): ').upper().strip()
        if sexo == 'M' or sexo == 'F':
            dici['sexo'] = sexo
            break
        else:
            print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')

    dici['idade'] = int(input('Idade: '))
    
    print('=' * 50)
    print('Cadastro finalizado:')
    print(dici)
    print('=' * 50)
    
    continuar = input('Deseja cadastrar outra pessoa? (s/n): ')
    if continuar.lower() != 's':
        break
