
v1 = int(input("Digite o primeiro valor inteiro positivo: "))
v2 = int(input("Digite o segundo valor inteiro positivo: "))
v3 = int(input("Digite o terceiro valor inteiro positivo: "))


maior_valor = v1
menor_valor = v1


if v2 > maior_valor:
    maior_valor = v2
elif v2 < menor_valor:
    menor_valor = v2

if v3 > maior_valor:
    maior_valor = v3
elif v3 < menor_valor:
    menor_valor = v3


media = (v1+ v2+ v3) / 3


print("O maior valor é:", maior_valor)
print("O menor valor é:", menor_valor)
print("A média dos valores é:", media)



