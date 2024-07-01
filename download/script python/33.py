homens=0
maior=0
menores=0


while True:
    print('-'*50)
    print('\t CADASTRE UMA PESSOA')
    print('-'*50)
    idade=int(input('idade:'))
    sexo=input('SEXO [M/F]').upper().strip()[0]
    if idade > 18:
        maior=maior + 1
    elif sexo == 'M':
        homens=homens+ 1
    elif sexo == "F" and idade < 20:
        menores=menores+1

    print('-'*50)

    desejo=input(' QUER CONTINUAR? [S/N]').upper().strip()[0]
    if desejo == 'N':
        break
    

print(f'''      total de pessoas com mais de 18 anos: {maior}
       total de homens cadastrados: {homens}
       total de mulheres menores de 20 {menores}''' )