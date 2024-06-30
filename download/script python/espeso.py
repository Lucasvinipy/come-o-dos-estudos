import os
os.system('cls')
print('\t\tpeso ideal')
peso=float(input('seu peso em kilos:'))

if peso > 0 and peso < 300:
    altura=float(input('sua altura em metros:'))

    if altura > 0 and altura < 3:
        massa=peso/altura**2
        
        if massa < 26:
            print('normal')
        elif massa >= 26 and massa < 30:
            print('obeso')
        else:
            print('obeso morbido')
    else:
        print('altura invalida')
else:
    print('peso invalido')

