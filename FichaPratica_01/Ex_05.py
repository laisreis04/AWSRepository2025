# Solicitar 2 numeros
num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))

#Verificar quem é o maior
if num1 < num2:
    maior = num2
    menor = num1
elif num1 == num2:
    print("Numeros iguais")
else:
    menor = num2
    maior = num1

# Imprimir
print(f"O maior é: {maior} e o menor {menor}")