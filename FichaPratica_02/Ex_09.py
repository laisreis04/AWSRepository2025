#Input
numPedido =  int(input("Insira um número: "))


# condição para ter a certeza que é maior que 2
if numPedido > 2 :
    numero = 2
    while numero <= numPedido:
        print(numero)
        numero += 2
        