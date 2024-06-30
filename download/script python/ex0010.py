lista=[]
dados=[]

while True:
    dados.append(input('nome :'))
    dados.append(float(input('peso :')))
    lista.append(dados[:])
    dados.clear

    escolha=input('quer continuar? [S/N]').upper().strip()[0]
    
    if escolha not in "S":
        if escolha == 'N':
            print('progama finalizado , informaçoes abaixo')
            break
        else:
            print('opção invalida')

    
maior=max(lista)
    
    
print(maior)
