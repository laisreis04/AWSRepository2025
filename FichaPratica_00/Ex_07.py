#solicitar  input - 3 valores
preco1 = float(input("Valor do 1º porduto = " ))
preco2 = float(input("Valor do 2º porduto = " ))
preco3 = float(input("Valor do 3º porduto = " ))

#calcular o total
total = preco1 + preco2 + preco3

#Aplicar desconto
totalComDesconto = total * 0.9

#Imprimir o resultado
print("Total da compra é de : ",totalComDesconto)