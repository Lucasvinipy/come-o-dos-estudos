def fatorial(num=1):
    f=1
    for c in range(num , 0 , -1):
        f = f * c

    return f
f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()

print(f'o resultado é {f1} {f2} {f3}')