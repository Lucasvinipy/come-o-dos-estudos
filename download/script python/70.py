print('progama teste')
lista=[]
listaimpar=[]
listapar=[]


while True:
    lista.append(int(input('escolha um numero:')))
    
    escolha=input('deseja continuar: [S/N]').upper().strip()[0]
    if escolha not in 'S ' and 'N':
        break   
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)

    
print(lista)
print(listapar)
print(listaimpar)


