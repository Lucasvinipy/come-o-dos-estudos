print('sr manuel')

num=int(input('quatidade de itens : '))
soma=0
for c in range(num):
    soma=soma + 1.99

soma_formatada = '{:.2f}'.format(soma)

print('Total a pagar: R$', soma_formatada)
