import os
os.system('cls')

print('sistema de peixes')
peso_peixes=float(input('peso em kilos do peixe:'))

if peso_peixes >50:
    execesso=peso_peixes-50
    multa=execesso*4
elif peso_peixes >0 and peso_peixes<50:
    execesso=0
    multa=0
else:
    execesso=0
    multa=0
    print('peso invalido')


print(execesso,multa)



