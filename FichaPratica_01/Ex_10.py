#Solicitar 2 numeros
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
#Solicitar a operação
operacao = input("Insira a operação (+,-,*,/): ")

#Realizar a operação
if operacao == '+':
    resultado = num1 +num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro ! Não dá para dividir por 0"
elif operacao == '*':
    resultado = num1 * num2
else:
    resultado = "Operação inválida"

#Imprimir o resultado
print ("Resultado = ", resultado)