import random

letras = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "Ñ",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = [
    "!",
    "¡",
    "@",
    "#",
    "$",
    "%",
    "&",
    "/",
    "(",
    ")",
    "=",
    "*",
    "+",
    "¿",
    "?",
    "-",
    "_",
    "{",
    "}",
]

print("Bienvenidos al generador de contraseñas")
numero_letras = int(input("¿Cuántas letras necesita? "))
numero_numeros = int(input("¿Cuántos numeros necesita? "))
numero_simbolos = int(input("Cuántos simbolos necesita? "))

lista = []

for letra in range(1, numero_letras + 1):
    valor = random.choice(letras)
    lista.append(valor)

for letra in range(1, numero_letras + 1):
    valor = random.choice(numeros)
    lista.append(valor)

for letra in range(1, numero_letras + 1):
    valor = random.choice(simbolos)
    lista.append(valor)

random.shuffle(lista)
print("Contraseña: {}".format("".join(lista)))
