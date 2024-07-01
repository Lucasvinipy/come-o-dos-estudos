print('testador')
num1=int(input('digite o primeiro numero:'))
num2=int(input('digite o segundo numero:'))
if num1 > num2:
    print('o maior numero entre {} e {} é igual a {}'.format(num1,num2,num1))
elif num2 > num1:
    print('o maior numero entre {} e {} é igual a {}'.format(num1,num2,num2))
else:
    print('os numeros possuem o mesmo valor')