def notas():
    notas_lista = []
    while True:
        nota = input('Nota: ')
        if nota.replace('.', '', 1).isdigit():
            nota = float(nota)
            notas_lista.append(nota)
        else:
            print('Por favor, insira um valor numérico válido.')
            continue

        while True:
            continuar = input('Deseja cadastrar outra nota (S/N): ').upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                dici = {}
                dici['total'] = len(notas_lista)
                dici['maior'] = max(notas_lista)
                dici['menor'] = min(notas_lista)
                media = sum(notas_lista) / len(notas_lista)
                dici['media'] = media
                return dici
            else:
                print('Por favor, digite S para sim ou N para não.')

def ver(dici, sit=False):
    decisao = input('Ver situação: [S/N] ').upper().strip()
    if decisao == 'S' and sit:
        if dici['media'] > 7:
            dici['situação'] = 'boa'
        elif dici['media'] > 5:
            dici['situação'] = 'razoável'
        else:
            dici['situação'] = 'ruim'
    return dici

# Chamada das funções
dicionario_notas = notas()
resultado = ver(dicionario_notas, sit=True)
print(resultado)
