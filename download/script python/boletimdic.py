dici={}
litsa=[]

while True:
    dici['nome']=input('nome:')
    dici['media']=float(input(f'media de {dici['nome']}:' ))
    if dici['media'] >= 5:
        dici['situação'] = 'aprovado'
    elif dici['media'] < 3:
        dici['situação'] = 'reprovado'
    else:
        dici['situação'] = 'exame'
    
    litsa.append(dici.copy())

    continuar=input('continuar [S/N]').upper().strip()[0]

    if continuar not in 'SN':
        print('opçao invalida gerando novamente...')

    elif continuar =='S':
        print('='*50)
    else:
        break

    

print('='*50)

for dici in litsa:
    for n , r in dici.items():
        print(f' {n:<10} é   igual   a {r:>10}')
        print('='*50)
