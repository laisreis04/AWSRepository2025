# Inputs
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))


# Comparar o primeiro com o segundo
if numero1 > numero2:
    # Troca os números se estiverem fora de ordem
    temp = numero1
    numero1 = numero2
    numero2 = temp

# Comparar o segundo (que pode ter sido trocado) com o terceiro
if numero2 > numero3:
    # Troca os números se estiverem fora de ordem
    temp = numero2
    numero2 = numero3
    numero3 = temp

# Comparar novamente o primeiro com o segundo
if numero1 > numero2:
    # Trocar os números se estiverem fora de ordem
    temp = numero1
    numero1 = numero2
    numero2 = temp

# Imprimir
print("Números em ordem crescente:", numero1, numero2, numero3)