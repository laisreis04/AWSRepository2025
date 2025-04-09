#input 1
num1 = float(input("Insira o 1º número: "))
#input 2
num2 = float(input("Insira o 2º número: "))
# input 3
num3 = float(input("Insira o 3º número: "))


#Calcular média + pesos
mediaAritmetica = (num1 + num2 + num3) / 3

mediaPonderada = (num1 * 0.2) + (num2 *0.3) + (num3 * 0.5)

#Imprimir o resultado
print("Média Aritmética: ",mediaAritmetica)
print("Média Ponderada = ",mediaPonderada)