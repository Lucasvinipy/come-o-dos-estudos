def contador(a,b,c):
    for c in range(a,b,c):
        print(c )
        print('='*50)
    

contador(1,10,1)

contador(10,1,-1)
print('AGORA É SUA VEZ ESCOLHA')
incio=int(input('INICIO :'))
fim=int(input('final : '))
passo=int(input('passo : '))
contador(incio,fim,passo)

