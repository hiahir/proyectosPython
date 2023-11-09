import math


def calcular_numero_botes(alto, ancho, cubre):
    valor = (alto * ancho) / cubre
    numero_botes = math.ceil(valor)
    return numero_botes


alto = int(input("¿Cual es el alto de la pared? "))
ancho = int(input("¿Cual es el ancho de la pared? "))
cubre = float(input("¿Cuantos metros cuadrados cubre cada bote de pintura? "))

numero_botes = calcular_numero_botes(alto, ancho, cubre)
print(f"El numero de botes de pintura que tengo que comprar es de {numero_botes}")
