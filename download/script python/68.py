lista=[]
while True:
    lista.append(int(input('digite um valor:')))
    escolha=input('quer continuar? [S/N]').upper().strip()[0]

    if escolha == 'N':
         break
    
    
    
print(lista.sort())
