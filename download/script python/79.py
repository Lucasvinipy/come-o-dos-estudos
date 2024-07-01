print('progama que le numeros reais')
dentro=[]
lista = []
quantiade=0


for c in range(10):
    lista.append(float(input(f'digite o { c + 1} numero : ')))


for c in lista:

    if c > 3.5 and c < 7.5:
        quantiade=quantiade + 1 
        dentro.append(c)


print('a lista completa é ',*lista , sep='  ')
print('os numeros entre 3,5 e 7,5 sao :', *dentro)
print(f'a quantidad de numeros entre 3,5 e 7,5 é {quantiade}')