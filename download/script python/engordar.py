#progama que calcula engordar 15% e emegrecer 20%


print('projeção de peso')
pesokg=float(input('quantidad de massa corporal em kilos:'))
engordar=(pesokg/100*15)+pesokg
emagrecer=pesokg - 100*20/pesokg
print(engordar , emagrecer )