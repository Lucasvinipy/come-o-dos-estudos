import random 
import os 
ale=(random.randint(0,10),random.randint(0,10) , random.randint(0,10) , random.randint(0,10) ,random.randint(0,10))
for c in ale:
    print(c)
print(f'o maior numero é {max(ale)}')
print(f'o menor  numero é {min(ale)}')