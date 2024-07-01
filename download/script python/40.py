import os
os.system('cls')

print('receita federal') 

nome=input('nome:')
cpf=input('CPF:')
renda_anual=float(input('renda anual:'))

if renda_anual > 0:
    dependentes=int(input('dependentes:'))
    desconto=1100*dependentes
    rendaliquida=renda_anual-desconto

    if rendaliquida <= 800:
        print('isento')
    elif rendaliquida >800 and rendaliquida<= 4000:
        imposto= rendaliquida*0.025+rendaliquida
        print(imposto)
    elif rendaliquida > 4000 and rendaliquida <= 9000:
        imposto= rendaliquida * 0.05+rendaliquida
        print(imposto)
    else:
        imposto=rendaliquida*0.10+rendaliquida
        print(imposto)
else:
    print('renda invalida')
