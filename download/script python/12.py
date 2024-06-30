import random

p1 = str(input('Digite o nome da primeira pessoa: '))
p2 = str(input('Digite o nome da segunda pessoa: '))
p3 = str(input('Digite o nome da terceira pessoa: '))

op = [p1, p2, p3]
random.shuffle(op)

print("Sequência embaralhada:", op)


