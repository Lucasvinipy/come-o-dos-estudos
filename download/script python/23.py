print('emprestimo bancario')
vc=float(input('digite o valor da casa'))
salario=float(input('digite o seu salario:'))
anos=int(input('quantos anos:'))
prestacaoanual=vc/12
pestacaomensal=prestacaoanual/12
porcentagem = (salario / 100 * 30) 
if pestacaomensal > porcentagem:
    print('emprestimo negado')
else:
    print('parabens ')