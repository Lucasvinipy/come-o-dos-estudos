print('media')
media=float(input('digite sua media'))
if media > 0 and media <= 10:

    if media >= 5:
        print('aprovado')
    elif media >= 3 and media < 5:
        print('exame')
    else:
        print('reprovado')
else:
    print('media invalida')