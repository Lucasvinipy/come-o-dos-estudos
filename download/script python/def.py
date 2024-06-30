lista=[]




def mutplicaçao(a,b):
    mult=a * b
    
    print(mult)
    print('='*50)
    print(f'a area de um terreno {a} x {b} é {mult}')
    lista.append(mult)
    
    



while True:
    a=float(input('altura : '))
    b=float(input('largura : '))


    mutplicaçao(a,b)
    while True:
        continuar = input('Deseja cadastrar outra pessoa? (S/N): ').upper().strip()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            print('Por favor, digite S para sim ou N para não.')
    
    if continuar == 'N':
        break




for c , p  in enumerate(lista):
    print(f'o {c + 1} terreno tem area de : {p}')