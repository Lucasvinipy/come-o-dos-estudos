print('Estudo 3 Cibeluda')

lista = []
pos = 0
neg = 0


for c in range(10):
    numero = float(input(f'Digite o {c + 1}º número: '))
    lista.append(numero)


    if numero > 0:
        pos += 1
    elif numero < 0:
        neg += 1

lista.sort(reverse=True)
print(*lista , sep= '-')
media = sum(lista) / 10


maior = max(lista)
menor = min(lista)


print(f'Quantidade de números negativos: {neg}')
print(f'Quantidade de números positivos: {pos}')
print(f'Média dos números: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
