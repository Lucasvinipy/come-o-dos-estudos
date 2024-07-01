print('estudo utlizando cibeluda')
lista=[]

for c in range(10):
    lista.append(int(input(f'digite o {c + 1} numero:  ')))

print(*lista , sep= '\n')