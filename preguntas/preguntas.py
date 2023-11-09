print("Bienvenidos al juego de preguntas")

respuesta1 = input(
    "¿Quieres ir a la izquierda o la derecha ?. Escribe 'izquierda' o 'derecha'"
).lower()

if respuesta1 == "izquierda":
    print(
        "Respuesta erronea. Te has caido en un agujero y has perdido. Puedes volver a intentarlo"
    )
else:
    respuesta2 = input(
        "Tienes que cruzar a una isla. ¿Quieres ir nadando o quieres esperar una barco para cruzar. Escribe 'nadar' o 'esperar'"
    ).lower()
    if respuesta2 == "nadar":
        print(
            "Respuesta erronea. Había tiburones. Has perdido. Puedes volver a intentarlo"
        )
    else:
        respuesta3 = input(
            "Has llegado a una casa que tiene tres puertas. Una de color azul, otra de color rojo y otra de color verde. ¿Qué puerta quieres abrir? Escribe 'azul', 'rojo' o 'verde'"
        ).lower()
        if respuesta3 != "verde":
            print("Respuesta erroena. Has perdido. Puedes volver a intentarlo")
        else:
            print("Enhorabuena. Has ganado.")
