print('progama teste')
lista=[]


while True:
    lista.append(int(input('escolha um numero:')))
    escolha=input('deseja continuar: [S/N]').upper().strip()[0]


    if escolha not in 'S ' and 'N':
        break
    
print(len(lista))

lista.sort(reverse=True)

print(lista)

for c  in lista:
    if c == 5:
        print(f'o numero 5 esta na lista na posição {c}')
        break
    else:
        print('o numero 5 nao esta nessa lista')