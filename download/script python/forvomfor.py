lista = []
dentro = []

soma = 0 
mult7 = 0

for c in range(9):
    lista.append(int(input(f'digite o { c + 1} numero : ')))

for p in lista:
    if p % 5 == 0:
        soma=soma + p
        dentro.append(p)

    elif p % 7 == 0 :
        mult7=mult7 + 1
        dentro.append(p)


print('a lista completa é' , *lista  )
print('os mutiplos de 7 e 5 são ',*dentro)
print(f'a soma dos mutiplos de 5 é {soma } e a quantidad de mutiplos de 7 é {mult7}')