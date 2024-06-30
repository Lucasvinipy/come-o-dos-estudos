import datetime
print('alistamento')
atual=datetime.date.today().year
nasc=int(input('digite a data de nascimento'))
idade=atual - nasc
if idade == 18:
    print('esta na hora de se alistar')
elif idade > 18:
    falta= idade - 18 
    print('voce tem {} anos e passou {} anos do tempo '.format(idade,falta))
else:
    falta= 18 - idade 
    print('voce nao tem idade para se alistar faltam {} anos '.format(falta))