import unittest
from coches import *

class test_clase_padre(unittest.TestCase):
    def preparar_datos_conexion(self):
        borrar_datos()
        
        datos = leer_datos(nombre_fichero)
        conexion = crear_conexion_bd()
        crear_tabla_coches(conexion)
        grabar_coche(conexion, datos)
        return conexion


nombre_fichero = "test.csv"
class test_numero_coches_tabla(test_clase_padre):
    def test(self):
        conexion = self.preparar_datos_conexion()
        
        dato = numero_de_coches(conexion)
        self.assertEqual(2780, dato)


class test_precio_total_coches(test_clase_padre):
    def test2(self):
        conexion = self.preparar_datos_conexion()
        
        dato = precio_total_de_coches(conexion)
        dinero = "{:,}".format(dato).replace(",",".")
        self.assertEqual("38.997.136.0", dinero)

if __name__ == "__main__":
    unittest.main()