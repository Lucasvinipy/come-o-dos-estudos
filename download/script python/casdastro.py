import time
import os

os.system('cls')


print('progama de cadastro')

dic={}

while True:
    dic['nome']=input('nome : ')
    dic['ano nascimento']=int(input('ano que nasceu: '))
    dic['CTPS']=int(input('carteira de trbalho :'))
    dic['ano contratada']=int(input('primeiro emprego : '))
    dic['salario']=float(input('salario : '))

    if dic['CTPS']== 0:
        print('=')
        break
    tempo_atual = time.localtime()
    ano_atual = tempo_atual.tm_year
    idade=ano_atual-dic ['ano nascimento'] 
    dic['idade']=idade
    del dic['ano nascimento']
    aposentadoria= (ano_atual-dic['ano contratada']  - 40 ) * -1
    dic['aposentadoria']=aposentadoria

    

    break
os.system('cls')
print('='*50)
for c , v in dic.items():
    print(f'{c:>20}     iguaL   {v:>10} \n {'='*50}')

