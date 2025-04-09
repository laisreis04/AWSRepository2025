#Ler dois números (Input)
numero1 = int(input("Insira o 1º número: "))
numero2 = int(input("Insira o 2º número: "))

#Mostar o maior entre eles - Verificar
if numero1 > numero2:
    maior = numero1
#Pode já imprimir aqui
else:
    maior = numero2

#Imprimir
#print(f"Maior número é = {maior}")
print("O maior número é : ", maior)