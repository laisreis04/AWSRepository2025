# Pedir input (Salto e Numero limite)
numLimite = int(input(" Insira o numero limite: "))
numSalto = int(input(" Insira o numero salto: "))

#Condição
if numLimite > 0 and numSalto > 0:
    contador = 0 # pode ser definido antes
    while contador <= numLimite:
        print(contador)
        contador += numSalto #contador = contador + numSalto


    

