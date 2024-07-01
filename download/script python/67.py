print('lista de pares e impares')
lista=[]
listapar=[]
listaimpar=[]

while True:
    numero=int(input('numero : '))
    lista.append(numero)


    wanted=input('continuar [S/N]').upper().strip()[0]

    if wanted not in "SN":
        print('opçao invalida')
    elif wanted == 'S':
        print ('-'*50)
    else:
        break

for c in lista:

    if c % 2 == 0:
        listapar.append(c)

    else:
        listaimpar.append(c)

listaimpar.sort()
listapar.sort()
print(f'a lista inteira{lista}')
print(f'os numeros imapres {listaimpar}')
print(f'os numeros pares {listapar}')