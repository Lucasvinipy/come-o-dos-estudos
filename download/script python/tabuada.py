print('\t tabuada')

cont=1
while True:
    num=int(input('digite o numero da tabuada:'))
    calc=num*(cont+1)
    if num < 0:
        print('progama encerrado')
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
        print('pressione enter para continuar')
        input()
