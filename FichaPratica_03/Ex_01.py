#Guardar numa variavel se o o user quer sair
saidaVar = "s"


for i in range(100):
    

    num01 = float(input("Insira o 1º valor: "))
    num02 = float(input("Insira o 2º valor: "))
    opcao = input("Insira qual o tipo de operação: ")
    continuar = input("Continuar a operação: (s = Sair / c = Continuar)")

    if continuar == "s":  
        break  
    if continuar == "c":
        #Fazer os if com as opções da operações....