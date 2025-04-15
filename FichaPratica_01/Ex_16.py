# Input
valor = int(input("Insira o valor em euros (múltiplo de 5): "))

# Verificar o número
if valor % 5 != 0:
    print("Valor inválido. Insira um múltiplo de 5.")
else:
    
    nota_200 = 200
    nota_100 = 100
    nota_50 = 50
    nota_20 = 20
    nota_10 = 10
    nota_5 = 5

    # Calcular a quantidade de cada nota
    quantidade_200 = valor // nota_200
    if quantidade_200 > 0:
        print(f"{quantidade_200} notas de {nota_200} euros")
        valor %= nota_200

    quantidade_100 = valor // nota_100
    if quantidade_100 > 0:
        print(f"{quantidade_100} notas de {nota_100} euros")
        valor %= nota_100

    quantidade_50 = valor // nota_50
    if quantidade_50 > 0:
        print(f"{quantidade_50} notas de {nota_50} euros")
        valor %= nota_50

    quantidade_20 = valor // nota_20
    if quantidade_20 > 0:
        print(f"{quantidade_20} notas de {nota_20} euros")
        valor %= nota_20

    quantidade_10 = valor // nota_10
    if quantidade_10 > 0:
        print(f"{quantidade_10} notas de {nota_10} euros")
        valor %= nota_10

    quantidade_5 = valor // nota_5
    if quantidade_5 > 0:
        print(f"{quantidade_5} notas de {nota_5} euros")
        valor %= nota_5