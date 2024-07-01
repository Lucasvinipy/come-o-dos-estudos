

def escreva(txt):
    print(len(txt) * '=')  
    print(f'{txt:>5}')            
    print(len(txt) * '=')  


frase=input('frase : ')

escreva(frase)
