#Solicitar saldo
saldoInicial = float(input("Introduza o saldo inicial: "))
#Valor para movimentar
valorMovimentar = float(input("Introduza o valor a movimentar: "))

#Atulizar saldo
saldoAtual = saldoInicial + valorMovimentar

#Verificar se o saldo é suficiente + Imprimir
if saldoAtual >= 0:
    print("Saldo atual: ", saldoAtual)
else:
    print("Saldo insuficiente: ", saldoInicial, "->", saldoAtual)
