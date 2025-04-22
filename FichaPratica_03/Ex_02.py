for _ in range(100):
    print("Menu de opções:")
    print("1. Criar")
    print("2. Atulizar")
    print("3. Eliminar")
    print("4. Sair")

    #Input da opção do user

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Opção 1 selecionar - Criar")
    elif opcao == "2":
        print("Opção 2 selecionar - Atualizar")
    elif opcao == "3":
        print("Opção 3 selecionar - Eliminar")
    elif opcao == "4":
        print("Opção 4 selecionar - Sair")
        break
    else:
        print("Opção Inválida")
        
