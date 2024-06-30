import os
os.system('cls')
print('-'*50)
print('\t LOJA SUPER BARATÃO')
print('-'*50)
total=0
acima=0
barato=0
while True:
    nome=input("nome do produto:")
    preco=float(input('preço: R$'))
    mais=input('quer algo mais? [S/N]').upper().strip()[0]
    if mais == 'N':
        break
    total =  total + preco 
    if preco > 1000:
        acima = acima + 1
    
    
