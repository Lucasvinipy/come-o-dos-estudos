
print('progama das notas')

quantide=int(input('digite quantos alunos tem: '))
soma=0
for c in range(quantide):
   nota=float(input('digite a nota: '))
   nota2=float(input('digite a nota: '))
   soma=nota+nota2+soma

print(soma)
media= soma / quantide

print(media)



    