def jogador(a='desconhecido',b=0):
    print(f'o jogador {a} fez {b}') 



a=input('nome do jogador : ')
b=input('gols : ')
if b.isnumeric():
    b=int(b)

else:
    b=0

if a.strip() == ' ':
    jogador(b=0)

else:
    jogador(a,b)    