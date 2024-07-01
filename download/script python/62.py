print('BOLETIM')
import os

os.system('cls')

princ = []
temp = []

while True:
    nome = input("Nome: ")
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))

    media = (nota1 + nota2) / 2

    temp.extend([nome, media, nota1, nota2])
    princ.append(temp[:])
    temp.clear()

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar not in "NS":
        print('Opção inválida')
    elif continuar == 'S':
        print('==' * 50)
        os.system('cls')
    else:
        break

print('==' * 50)
print(f'{"ID":<4} {"NOME":<10} {"MEDIA":>5}')
print('==' * 50)
for c, l in enumerate(princ):
    print(f'{c:<4} {l[0]:<10} {l[1]:>5.1f}')
print('=' * 50)
print('Digite o número do aluno para ver as notas ou 999 para parar')
print('=' * 50)

while True:
    escolha = input('Aluno (ID): ')
    if escolha == '999':
        break

    try:
        escolha = int(escolha)
        if 0 <= escolha < len(princ):
            aluno = princ[escolha]
            print(f'Aluno: {aluno[0]}')
            print(f'Notas: {aluno[2]}, {aluno[3]}')
        else:
            print('ID de aluno inválido.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido.')

print('Programa encerrado.')
