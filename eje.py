# Estructura de control IF
numeroIf = 5

if numeroIf > 0:
    print("El número es positivo")
elif numeroIf < 0:
    print("El número es negativo")
else:
    print("El número es 0")

# Estructura de control WHILE
numeroWhile = 0

while numeroWhile < 3:
    numeroWhile += 1
    print(f"El número es {numeroWhile}")

# Estructura de control DO WHILE
numeroDoWhile = 0

do:
    numeroDoWhile += 1
    print(f"El número es {numeroDoWhile}")
while numeroDoWhile < 3

# Estructura de control FOR
numeroFor = 0

for i in range(4):
    numeroFor += 1
    print(f"El número es {numeroFor}")

# Estructura de control SWITCH
estacion = "otoño"

def mostrarMensaje(estacion):
    switcher = {
        "verano": "Estamos en verano",
        "otoño": "Estamos en otoño",
        "invierno": "Estamos en invierno",
        "primavera": "Estamos en primavera"
  }
    return switcher.get(estacion, "No es una estación válida")

print(mostrarMensaje(estacion))
