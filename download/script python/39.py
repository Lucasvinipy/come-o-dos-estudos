while True:
    nome = input("Atleta: ")
    if not nome:
        break
    
    saltos = []
    for i in range(1, 6):
        salto = float(input(f"{i}º Salto: "))
        saltos.append(salto)
    
    media = sum(saltos) / len(saltos)
    
    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media:.1f} m\n")


    

        
