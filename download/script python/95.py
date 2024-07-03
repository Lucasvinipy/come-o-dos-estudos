def converte_moeda(valor, taxa_cambio, tipo_conversao):
    if tipo_conversao == "A para B":
        valor_convertido = valor * taxa_cambio
    elif tipo_conversao == "B para A":
        valor_convertido = valor / taxa_cambio
    else:
        return "Tipo de conversão inválido"
    return valor_convertido


valor = float(input('Digite o valor a ser convertido: '))
taxa_cambio = float(input('Digite a taxa de câmbio: '))
tipo_conversao = input('Digite o tipo de conversão (A para B ou B para A): ')

resultado = converte_moeda(valor, taxa_cambio, tipo_conversao)
print(f'O valor convertido é: {resultado}')
