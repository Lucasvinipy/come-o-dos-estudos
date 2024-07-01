import os
os.system('cls')
print('conta de hospedagem:')
nome_hospede=str(input('nome do hospede:'))
tipo_apartamento=str(input('modelo de apartamento:'))
num_diarias=int(input('numero de diarías:'))
valor_consumo=float(input('valor do consumo interno:'))
 
 
if tipo_apartamento == 'a':
    valor_diaria= 150 * num_diarias
    subtototal=valor_diaria+valor_consumo
    taxa=subtototal/100*10+subtototal
    print('o gasto total foi',taxa)
elif tipo_apartamento == 'b':
    valor_diaria=100 * num_diarias
    subtototal=valor_diaria+valor_consumo
    taxa=subtototal/100*10+subtototal
    print('o gasto total foi',taxa)
elif tipo_apartamento == 'c':
    valor_diaria= 75 * num_diarias
    subtototal=valor_diaria+valor_consumo
    taxa=subtototal/100*10+subtototal
    print('o gasto total foi',taxa)
elif tipo_apartamento == 'd':
    valor_diaria= 50 * num_diarias
    subtototal=valor_diaria+valor_consumo
    taxa=subtototal/100*10+subtototal
    print('o gasto total foi',taxa)
else:
    print('modelo de apartamento invalido')