# Input Horas
horas = int(input("Insira as horas (0-23): "))

# Input Minutos
minutos = int(input("Insira os minutos (0-59): "))

# Converter para o formato 12 horas
if 0 <= horas <= 23 and 0 <= minutos <= 59:
    if horas == 0:
        horas_12h = 12
        periodo = "AM"
    elif horas < 12:
        horas_12h = horas
        periodo = "AM"
    elif horas == 12:
        horas_12h = 12
        periodo = "PM"
    else:
        horas_12h = horas - 12
        periodo = "PM"

    # Imprimir
    print(f"{horas:02}:{minutos:02} é {horas_12h:02}:{minutos:02} {periodo}")
else:
    print("Horário inválido")