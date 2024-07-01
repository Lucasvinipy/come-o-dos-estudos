print('BOLETIM  ')
import os 


os.system('cls')

princ=[]
temp=[]


while True:

    nome=input("Nome : ")
    nota1=float(input('primeira nota : '))
    nota2=float(input('segunda Nota : '))

    media=(nota1+nota2) / 2


    temp.extend([nome,media,nota1,nota2])


    princ.append(temp[:])
    
   
    temp.clear()
    

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar not in "NS":
        print('opção invalida')

    elif continuar == 'S':
        print('=='*50)
        os.system('cls')

    else:
        break 

print('=='*50)
print('ID     NOME      MEDIA')
print('=='*50)
for c , l in enumerate(princ):
    print(f'{c} {l[0:2]}')
print('='*50)
print('digite o aluno ou 999 para parar')
print('='*50)


while True:

    escolha=input('aluno :')

    if escolha == '999':
        break

    for i , e in enumerate(princ):
        if escolha in e:
            print(f'o {e[0:1]} aluno  obteve as notas {e[2:4]}')
    







