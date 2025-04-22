#Input
numero = int(input("Insira um número: "))

if numero <= 1:
    print("Não é primo")
else:
    numDivisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            numDivisores += 1
    if numDivisores ==2:
        print("É primo")
    else:
        print("Não é primo")

