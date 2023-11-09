import sys
import os
from os import remove
from zipfile import ZipFile
import pandas as pd
import sqlite3
from sqlite3 import Error

BASE_DE_DATOS = "coches.db"

def precio_medio_por_marca(conexion: sqlite3.Connection) -> list:
    cursor = conexion.cursor()
    cursor.execute("SELECT marca, AVG(precio) FROM coches GROUP BY marca")
    datos = cursor.fetchall()
    return datos

def marca_coche_mas_barato(conexion: sqlite3.Connection) -> list:
    cursor = conexion.cursor()
    cursor.execute("SELECT marca, modelo, MIN(precio) FROM coches")
    datos = cursor.fetchall()
    return datos

def precio_total_de_coches(conexion : sqlite3.Connection) -> int:
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM(precio) FROM coches")
    dato = cursor.fetchall()
    numero = dato[0][0]
    return numero

def numero_de_coches(conexion : sqlite3.Connection) -> int:
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM coches")
    dato = cursor.fetchall()
    numero = dato[0][0]
    return numero

def consultar_coches(conexion : sqlite3.Connection):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM coches LIMIT 20")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def borrar_datos():
    try:
        remove(BASE_DE_DATOS)
    except FileNotFoundError:
        pass


def crear_conexion_bd() -> sqlite3.Connection:
    try:
        conexion = sqlite3.connect(BASE_DE_DATOS)
        return conexion
    except Error:
        print(Error)


def descomprimir_fichero(nombre : str):
    with ZipFile(nombre, "r") as zip:
        zip.extractall()


def leer_datos(nombre : str):
    datos = pd.read_csv(nombre, sep=";")
    return datos


def crear_tabla_coches(conexion : sqlite3.Connection):
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE coches(
            marca text,
            modelo text,
            combustible text,
            transmision text,
            estado text,
            matriculacion text,
            kilometraje integer,
            potencia real,
            precio real)"""
    )
    conexion.commit()


def insertar_tabla_coches(conexion : sqlite3.Connection, coche : tuple):
    cursor = conexion.cursor()
    cursor.execute(
        """INSERT INTO coches(
            marca,
            modelo,
            combustible,
            transmision,
            estado,
            matriculacion,
            kilometraje,
            potencia,
            precio)
            VALUES (?,?,?,?,?,?,?,?,?)""",
        coche,
    )
    conexion.commit()


def grabar_coche(conexion : sqlite3.Connection, datos : pd.DataFrame):
    for fila in datos.itertuples():
        marca = fila[1]
        modelo = fila[2]
        combustible = fila[3]
        transmision = fila[4]
        estado = fila[5]
        matriculacion = fila[6]
        kilometraje = fila[7]
        potencia = fila[8]
        precio = fila[9]

        coche = (
            marca,
            modelo,
            combustible,
            transmision,
            estado,
            matriculacion,
            kilometraje,
            potencia,
            precio,
        )

        insertar_tabla_coches(conexion, coche)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Error. Numero de parametros incorrecto. Puede faltar el nombre del archivo"
        )
    else:
        nombre_fichero = sys.argv[1]

        borrar_datos()
        descomprimir_fichero(nombre_fichero)
        datos = leer_datos(nombre_fichero)
        print(datos)
        
        conexion = crear_conexion_bd()
        crear_tabla_coches(conexion)
        grabar_coche(conexion, datos)
        
        print("\nConsultamos los datos de la tabla")
        consultar_coches(conexion)
        
        numero = numero_de_coches(conexion)
        print("\nEl numero de coches es de {}".format(numero))
        
        numero = precio_total_de_coches(conexion)
        dinero = "{:,}".format(numero).replace(",",".")
        print("\nEl precio total de los coches es de {}".format(numero))
        
        datos = marca_coche_mas_barato(conexion)
        marca = datos[0][0]
        modelo = datos[0][1]
        precio = datos[0][2]
        print("\nCoche mas barato. Marca = {}, modelo = {}, precio = {}".format(marca, modelo, precio))
        
        print("\nPrecio medio por marca\n")
        datos = precio_medio_por_marca(conexion)
        for dato in datos:
            marca = dato[0]
            precio = dato[1]
            print(marca,precio)
        
        
