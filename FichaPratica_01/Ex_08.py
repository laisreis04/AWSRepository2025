#Solicitar 3 inputs
nota1 = float(input("Nota 1 (0 -20): "))
nota2 = float(input("Nota 2 (0 -20): "))
nota3 = float(input("Nota 3 (0 -20): "))
#Calcular média ponderada
mediaPonderada = (nota1 *0.25) + (nota2 *0.35) + (nota3 * 0.40)

#Verificar se está aprovado
if mediaPonderada >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")

#Imprimir

print(f"Média Ponderada = {mediaPonderada}")