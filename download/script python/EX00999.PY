


print('jogo do numero')
num_escolhido= 3
escolha=int(input('escolha um numero de 0 a 5:'))
if escolha > 5 or escolha < 0:
    print('numero invalido')
elif escolha == num_escolhido:
    print('voce acertou')
else:
    print('voce perdeu')