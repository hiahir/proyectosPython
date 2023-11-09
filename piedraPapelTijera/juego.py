import random

print("Bienvenidos al juego")
usuario = int(input("¿Qué opcion quieres? Escribe '0' para piedra, '1' para papel y '2' para tijera: "))

ordenador = random.randint(0,2)

print("Usuario = " + str(usuario))
print(f"Ordernador = {ordenador}")

if usuario == 0 and ordenador == 2:
    print("Ha ganado el usuario")
elif usuario > ordenador:
    print("Ha ganado el usuario")
elif usuario == ordenador:
    print("Empate")
else:
    print("Ha ganado el ordenador")
