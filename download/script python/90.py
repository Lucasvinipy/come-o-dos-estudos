import time

def maior(* num):
    cont=0
    maior=0
    for c in num:
        print(f'{c}' , end ='  ',flush=True)
        time.sleep(1)
        cont=cont+1
        if c > maior:
            maior = c

    print(f'o maior é {maior} e tem {cont} elementos')

    


maior(1,6,8,34,6,8)
maior(1,6,84,7)
maior(25,78,8)
maior(3,3)
maior()
