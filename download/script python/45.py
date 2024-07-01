import os
os.system("cls")

print('peso ideal ')
altura=float(input('altura:'))
if altura < 3:
    sexo=str(input('sexo:'))

    if sexo == 'masculino':
        peso_ideal=(72.7*altura)-58
        print(peso_ideal)
    elif sexo == 'feminino':
        peso_ideal=(62.1*altura)-44.7
        print(peso_ideal)
    else:
        print('sexo invalido')
else:
    print('altura invalida')
