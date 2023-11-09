print("Bienvenidos a la calculadora de propinas")
factura = float(input("¿Cuál es el importe de tu factura?"))
propina = int(input("¿Cuál es el procentaje de propina que quieres dejar?"))
personas = int(input("¿Entre cuántas personas hay que repartir la factura?"))

importe_propinas = (factura * propina) / 100
factura_total = factura + importe_propinas
importe_por_persona = factura_total / personas

print("El importe a pagar por persona es de " + str(round(importe_por_persona, 2)))
