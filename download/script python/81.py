import os
os.system('cls')

guarda = []
temp=[]
while True:
    print("\nMenu de Operações CRUD")
    print("1. Criar Funcionário")
    print("2. Ler Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Deletar Funcionário")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    

    if escolha == '1':
        nome = input('Nome: ')
        if any(elemento[0] == nome for elemento in guarda):
            print('Nome já cadastrado. \nPressione Enter para continuar...')
        else:
            temp.append(nome)
            temp.append(input('Email: '))
            temp.append(input('Cargo: '))
            guarda.append(temp[:])
            temp.clear()
            print('Funcionário cadastrado.\nPressione Enter para continuar...')
        input()
        os.system('cls')


        

    elif escolha == '2':
        for elemento in guarda:
            print(f'nome: {[elemento[0]]} email: {[elemento[1]]} cargo: {[elemento[2]]}')
        
        print('funcionarios lidos \n enter para continuar')

        input()
        os.system('cls')
    
    elif escolha == '3':
        nome=input('funcionario que deseja: ')
        for elemento in guarda:
            if elemento[0] == nome:
                print('nome localizado')
                novo_nome = input(f'Novo Nome ({elemento[0]}): ') or elemento[0]
                novo_email = input(f'Novo Email ({elemento[1]}): ') or elemento[1]
                novo_cargo = input(f'Novo Cargo ({elemento[2]}): ') or elemento[2]
                guarda[guarda.index(elemento)] = [novo_nome, novo_email, novo_cargo]
                print('Funcionário atualizado.\n Pressione Enter para continuar.')
    
                break
        else:
            print('funcionario nao encontrado')
        input()
        os.system('cls')

    elif escolha == '4':
        nome=input('funcionario que deseja excluir: ')
        for elemento in guarda:
            if elemento[0] == nome:
                print('funcionario localizado')
                guarda.remove(elemento)
                print('funcionario removido \n \n enter para continuar')
        else:
            print('funcionario nao existe')
        input()
        os.system('cls')

    elif escolha =="5":
        print('saindo do progama ')
        break
    else:
        print('opçao invalida \n enter para voltar')
        input()
        os.system('cls')