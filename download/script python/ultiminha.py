print('progama dos alunos')

lista = []

rep=0
ap=0
exame=0

while (rep + ap + exame) < 10:
    nota1=float(input('digite a primeira  nota :'))
    nota2=float(input('digite a segunda   nota :'))
   
    

    media = (nota1 + nota2) / 2

    if media > 5 and media < 10:
        ap=ap+1

    elif media > 3 and media < 5:
        exame=exame + 1
    
    else:
        rep=rep+1

print(ap,rep,exame)



