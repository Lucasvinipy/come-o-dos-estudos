import time


def nascimento(*a):
    ano=int(input('ano de nascimento : '))
    anoatual=time.localtime().tm_year
    idade=anoatual-ano
    if idade > 18 and idade < 65:
        print(f'com {idade} : VOTO OBRIGATORIO')
    elif idade >= 16 and idade > 65:
        print(f'com {idade} : : VOTO OPCIONAL')
    else:
        print(f'com {idade} : NAO VOTA')    



nascimento()