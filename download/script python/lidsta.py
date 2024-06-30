lista=['lucas', 'pedro' ,1 , 3 ,5 ,5 ,'spato']#todas listas começam em [0,1,2,3]

print(lista[2:3:1])# [inicio , final , passo] sempre acaba um numero antes
lista.append('roger')#adiciona no final da lista
lista.remove('lucas') # remove pelo elemento
del lista[1] # remove pelo indice
lista.pop(4) # remove pelo indice
lista.sort() # organiza a lista em ordem crescente 
lista.sort(reverse=True) # organiza em ordem decrecente
outra=lista[:] # copia lista sem mexer na anteririor
p=sum(lista) # soma da lsita
a=min(lista) # menor da lsita
c=max(lista) # maior da lista
t=len(lista) # tamanho da lista
xx=lista.count(7) # quantas vezes aapreceu na lista 
valor=lista.index(5) # primeira vez que aparece
lugar = lista.insert(4,'jorge')