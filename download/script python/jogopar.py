import random
import os
os.system('cls')

print('='*50)
print('jogo do par ou impar')
print('='*50)
computador=random.randint(1,11)
escolha=int(input('escolha um numero:'))
certe=input('[P/I]').upper().strip()[0]
venceu=0
while escolha > 0:
    jogada= escolha + computador

    if jogada % 2 == 0 and certe == "P":
        print(f'a soma deu {jogada} {('igual a par'if jogada % 2 == 0 else ' igual a impar')} , voce venceu')
        venceu=venceu+1
        escolha=int(input('escolha um numero:'))
        certe=input('[P/I]').upper().strip()
        os.system("cls")
    elif jogada % 2 == 0 and certe =='I':
        print(f'voce perdeu a {jogada} {('igual a par'if jogada % 2 == 0 else 'igual a impar')}, e voce escolheu{certe}')
        break
    elif jogada % 2 != 0 and certe == "I":
        print(f'voce venceu , a soma deu {jogada} {('igual a par'if jogada % 2 == 0 else 'igual a impar')}')
        venceu=venceu+1
        escolha=int(input('escolha um numero:'))
        certe=input('[P/I]').upper().strip()
        os.system('cls')
    else:
        print(f'voce perdeu , a soma deu {jogada} {('igual a par'if jogada % 2 == 0 else 'igual a impar')} e voce escolheu  {certe}')
        break
print(f'voce venceu {venceu} vezes')