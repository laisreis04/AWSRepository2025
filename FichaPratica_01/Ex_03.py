#Pedir input
salario = float(input("Insira o salário: "))

#Calcular
if salario <= 15000:
    imposto = salario *0.2
elif 15000 < salario and salario >= 20000:
    imposto = salario * 0.30
elif 20000 < salario <= 25000:
    imposto = salario *0.35   
else:
    imposto =salario *0.4

#Imprimir
print("imposto a pagar é de : ", imposto, "€")