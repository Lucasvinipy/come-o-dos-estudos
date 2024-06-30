print('emprestimo')
valorcasa=float(input('valor da casa:'))
salariomensal=float(input('salario mensal:'))
tempo=int(input('quantos anos:'))
presstacao=valorcasa/(tempo*12)
minimo=salariomensal/100*30
if minimo<= presstacao:
    print('ok')
else:
    print('nao')    
 