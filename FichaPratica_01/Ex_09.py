#Solicitar inputs
num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))
num3 = int(input("Insira o 3º número: "))

#Determinar qual o menor numero
menor = num1

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

#Imprimir

print("O menor número é: ", menor)