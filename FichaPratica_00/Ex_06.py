#Input -> int valor 1 e 2
valor1 = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))

#Usando ouma variavel extra
# temporariaV = valor1
# valor1 = valor2
# valor2 = temporariaV

#print("Valor 1 = ", valor1 )
#print("Valor 2 = ",valor2)

# troca sem a variavel extra
valor1, valor2 = valor2, valor1
print("Valor 1 = ", valor1 )
print("Valor 2 = ",valor2)

