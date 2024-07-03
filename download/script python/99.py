import random
import string

def gera_senha(comprimento):
    if comprimento < 4:  
        return "O comprimento da senha deve ser de pelo menos 4 caracteres."

   
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    
    senha += random.choices(todos_caracteres, k=comprimento - 4)

   
    random.shuffle(senha)

    senha = ''.join(senha)

    return senha

comprimento = int(input('Digite o comprimento da senha desejada: '))
senha_gerada = gera_senha(comprimento)
print(f'Senha gerada: {senha_gerada}')
