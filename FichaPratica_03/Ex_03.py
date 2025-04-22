#Garantir que o input seja apenas de 0 a 10

numeroSecreto = int(input("Insira o número secreto: "))

contadorTentativa = 0

for _ in range (10):
    contadorTentativa += 1
    palpiteJogador = int(input("Tente adivinhar o número secreto: "))
    if palpiteJogador < numeroSecreto:
        print("O número secreto é maior")
    elif palpiteJogador > numeroSecreto:
        print("O numero secreto é menor")
    else:
        print("Parbéns você acertou nº de tentativas", contadorTentativa, "o número secreto é: ", numeroSecreto)
        break

