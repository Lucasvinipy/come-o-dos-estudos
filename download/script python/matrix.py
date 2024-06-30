
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))


matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]


for l in range(linhas):
    for c in range(colunas):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))


print('-=' * 30)
for l in range(linhas):
    for c in range(colunas):
        print(f"[{matriz[l][c]:^5}]", end='')
    print() 
