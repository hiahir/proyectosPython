import replit
import random

def generar_carta():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = random.choice(cartas)
    return carta

def calcular_suma(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def mostrar_ganador(marcador_usuario, marcador_ordenador):
    if marcador_usuario == marcador_ordenador:
        texto = "Empate"
    elif marcador_ordenador == 0:
        texto = "Has perdido, el ordenador tiene 21 - Blackjack"
    elif marcador_usuario == 0:
        texto = "Has ganado !!! Tienes 21 - Balckjack"
    elif marcador_usuario > 21:
        texto = "Has perdido, la suma de tus cartas es mayor a 21"
    elif marcador_ordenador > 21:
        texto = "Has ganado !!! La suma de las de las cartas del ordenador es mayor a 21"
    elif marcador_usuario > marcador_ordenador:
        texto = "Has ganado !!!"
    else:
        texto = "Has perdido"
    return texto

def jugar():
    print("estamos jugando...")

    cartas_usuario = []
    cartas_ordenador = []
    finalizado = False

    for _ in range(2):
        carta = generar_carta()
        cartas_usuario.append(carta)

        carta2 = generar_carta()
        cartas_ordenador.append(carta2)

    print(f"Cartas del usuario {cartas_usuario}")
    print(f"Cartas del ordenador {cartas_ordenador}")

    while not finalizado:
        marcador_usuario = calcular_suma(cartas_usuario)
        marcador_ordenador = calcular_suma(cartas_ordenador)

        print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
        print(f"Cartas del ordenador = {cartas_ordenador[0]}, marcador = {marcador_ordenador}")

        if marcador_usuario == 0 or marcador_ordenador == 0 or marcador_usuario > 21:
            finalizado = True
        else:
            mas_cartas = input("¿Quieres mas cartas. Escribe 'si' o 'no': ").lower()
            if mas_cartas == "si":
                carta = generar_carta()
                cartas_usuario.append(carta)
            else:
                finalizado = True

    while marcador_ordenador != 0 and marcador_ordenador < 17:
        carta_ordenador = generar_carta()
        cartas_ordenador.append(carta_ordenador)
        marcador_ordenador = calcular_suma(cartas_ordenador)

    print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
    print(f"Cartas del ordenador = {cartas_ordenador}, marcador = {marcador_ordenador}")

    texto = mostrar_ganador(marcador_usuario, marcador_ordenador)
    print(texto)


# Principio del programa
while(input("¿Quieres jugar al blackjack?. Escribe 'si' o 'no': ").lower() == "si"):
    replit.clear()
    jugar()








