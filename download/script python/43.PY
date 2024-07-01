print('soma infinita')
soma=0
while True:
    num=int(input('digite um numero[999 para parar]:'))
    if num == 999:
        print('progama enecerrado')
        break
    soma=soma+num

print(soma)
