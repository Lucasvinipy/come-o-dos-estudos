lista = []

soma = 0 
mult7 = 0

for c in range(9):
    num=int(input(f'digite o { c + 1} numero : '))
    lista.append(num)

    if num % 5 == 0:
        soma=soma + num


    elif num % 7 == 0 :
        mult7=mult7 + 1
print(*lista )
print(soma , mult7)