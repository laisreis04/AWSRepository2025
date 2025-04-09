#Pedir dados - Input
salario = float(input("Insira o seu salário anual: "))

#Calcular salário
if salario <= 15000:
    imposto = salario * 0.2
    taxa = 20

else:
    imposto = salario *0.3
    taxa = 30

#Imprimir
print(f"Taxa a pagar é de ({taxa})% e o imposto é de {imposto}€")
