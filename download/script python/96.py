
def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    desconto = valor_conta * (porcentagem_gorjeta / 100)
    print(desconto)


valor_conta = float(input('Digite o valor da conta: '))
porcentagem_gorjeta = float(input('Digite a porcentagem da gorjeta: '))
calcula_gorjeta(valor_conta, porcentagem_gorjeta)








