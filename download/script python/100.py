def max_lista(lista):
    if not lista:  
        return None
    
    max_valor = lista[0]  
    for num in lista:
        if num > max_valor:
            max_valor = num
    return max_valor


lista = [int(x) for x in input('Digite uma lista de números separados por espaços: ').split()]
max_valor = max_lista(lista)
print(f'O maior valor da lista é: {max_valor}')
