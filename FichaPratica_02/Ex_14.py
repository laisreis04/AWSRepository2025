numero_fatorial = int(input("Introduza um número inteiro não-negativo: "))

if numero_fatorial < 0:
    print("Número inválido. Insira um número não-negativo.")
elif numero_fatorial == 0:
    print("Fatorial: 1")
else:
    fatorial_sem_multiplicacao = 1
    i = 1
    while i <= numero_fatorial:
        soma = 0
        j = 0
        while j < i:  # Simula a multiplicação por i
            soma += fatorial_sem_multiplicacao
            j += 1
        fatorial_sem_multiplicacao = soma
        i += 1
    print("Fatorial (sem *):", fatorial_sem_multiplicacao)

    