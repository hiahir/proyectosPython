import os


def calcular_ganador(apuestas):
    apuesta_maxima = 0
    ganador = ""
    for clave in apuestas:
        precio_apuesta = apuestas[clave]
        if precio_apuesta > apuesta_maxima:
            apuesta_maxima = precio_apuesta
            ganador = clave
    print(f"El ganador es {ganador} con un precio de {apuesta_maxima}")


print("Bienvenidos a la subasta")
apuestas = {}

mas_apuestas = True

while mas_apuestas:
    nombre = input("Nombre del apostante: ")
    precio = float(input("Precio de la apuesta: "))
    apuestas[nombre] = precio

    pregunta = input(
        "¿Hay mas personas que quieran hacer apuestas? Escribe 'si' o 'no'"
    ).lower()
    if pregunta == "si":
        os.system("clear")
    elif pregunta == "no":
        mas_apuestas = False

os.system("clear")
calcular_ganador(apuestas)
