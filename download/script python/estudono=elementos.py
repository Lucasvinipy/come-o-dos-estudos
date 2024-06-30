print('tabuada')

num=int(input('numero : '))
inicio=int(input('inicio : '))
fim=int(input('fim : '))
for c in range(inicio,fim):
    print(f'{num} x {(c + 1) - 1} = { num * c}')