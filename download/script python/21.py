#progama que calcula a vida bancaria de joao


print('salario de joao')    
salario_inicial=float(input('salario:'))
conta_1=float(input('conta atrasada 1:'))
conta_2=float(input('conta atrasada 2'))
total=salario_inicial-(conta_1/100*2+conta_1 + conta_2/100*2+conta_2)
print(total)