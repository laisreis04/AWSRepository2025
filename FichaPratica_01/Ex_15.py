# Inputs
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

# Input ordem
ordem = input("Escolha a ordem (Crescente ou Decrescente): ")

if ordem == "Crescente":
    
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    if numero2 > numero3:
        numero2, numero3 = numero3, numero2
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    print("Números em ordem Crescente:", numero1, numero2, numero3)

elif ordem == "Decrescente":
   
    if numero1 < numero2:
        numero1, numero2 = numero2, numero1
    if numero2 < numero3:
        numero2, numero3 = numero3, numero2
    if numero1 < numero2:
        numero1, numero2 = numero2, numero1
    print("Números em ordem Decrescente:", numero3, numero2, numero1)

else:
    print("Ordem inválida")