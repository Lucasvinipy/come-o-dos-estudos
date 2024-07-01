print('\t calculadora ')
n1=float(input('digite o numero:'))
n2=float(input('digite o numero:'))
print('''          [1] somar
          [2] mutiplicar
          [3] dividir
          [4] escolher outro numero
          [5] encerrar progama 

          ''')
op=int(input('\t----escolha sua opção------'))
while op > 5:
    print('opçao invalida')
    op=int(input('insira novamente:'))
while op <= 5:
    if op == 1:
        conta=n1+n2
        print('a soma entre {} e {} é {}'.format(n1,n2,conta))
    elif op == 2:
        conta=n1 * n2
        print('a mutiplicação entre {} e {} é {}'.format(n1,n2,conta))
    elif op ==3:
        conta  = n1 / n2
        print('a mutiplicação entre {} e {} é {}'.format(n1,n2,conta))
    elif op == 4:
        n1=float(input('digite o novo numero'))
        n2=float(input('digite o novo numero'))
    else:
        print('progama encerrado')
        
print('fim')
