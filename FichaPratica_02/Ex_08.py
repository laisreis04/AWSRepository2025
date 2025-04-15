soma = 0
contador = 0

while True: #colocar a condição para parar o ciclo 
    numero = int ( input("Insisra um número: "))
    if numero == -1:
        break
    soma += numero
    contador += 1
    if contador > 0:
        media = soma / contador
        print ("Média =  ", media)

