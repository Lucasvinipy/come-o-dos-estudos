print('estudo 2')

lista=[]

for c in range(10):
    lista.append(int(input(f'digite o {c + 1} numero : ')))

num=int(input('escolha um numero:'))

if num in lista:
    certo=lista.index(num)
    print(f'{num} encontrado na lista na posiçao {certo + 1}')
else:
    print('numero nao esta na lista')