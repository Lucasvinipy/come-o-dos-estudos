import math
angulo=float(input('digite o angulo'))
cosseno=math.cos(math.radians(angulo))
seno=math.sin(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print('o seno de {} é igual a {:.2f}\no cosseno de {} é igual a {:.2f}\na tangente de {} é igual a {:.2f}'.format(angulo,cosseno,angulo,seno,angulo,tangente))