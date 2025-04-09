#Input das musicas
musica1Minutos = int(input("Minutos música 1 : "))
musica1Segundos = int(input("Segundo música 1  : "))
musica2Minutos = int(input("Minutos música 2 : "))
musica2Segundos = int(input("Segundo música 2  : "))
# musica3Minutos = int(input("Minutos música 3 : "))
# musica3Segundos = int(input("Segundo música 3  : "))
# musica4Minutos = int(input("Minutos música 4 : "))
# musica4Segundos = int(input("Segundo música 4  : "))
# musica5Minutos = int(input("Minutos música 5 : "))
# musica5Segundos = int(input("Segundo música 5  : "))

totalSegundos = 0

#Somar minutos
minutosTotais = musica1Minutos + musica2Minutos 


segundoSoma = musica1Segundos + musica2Segundos 



#Converter a duração para segundos
totalSegundos += (minutosTotais * 60) + segundoSoma

#Calcular segundos, minutos e horas
horas = totalSegundos // 3600
minutos = (totalSegundos % 3600) // 60
segundo = totalSegundos % 60

#Apresentar o resultado
print(f"Tempo total = {horas}H{minutos}m{segundo}s")
print(horas,"H",minutos,"m",segundo,"s")