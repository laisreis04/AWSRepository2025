# Apresentar o menu
print("1. Criar")
print("2. Atualizar")
print("3. Eliminar")
print("4. Sair")

# Solicitar ao usuário que escolha uma opção
opcao = int(input("Escolha uma opção: "))

# Executar a ação 
if opcao == 1:
    print("Opção Criar selecionada")
elif opcao == 2:
    print("Opção Atualizar selecionada")
elif opcao == 3:
    print("Opção Eliminar selecionada")
elif opcao == 4:
    print("Sair")
else:
    print("Erro: Opção inválida")