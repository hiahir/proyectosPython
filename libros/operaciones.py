import sqlite3

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, isbn TEXT)")
    conexion.commit()
    conexion.close()


def insertar(titulo, autor, year, isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES (NULL,?,?,?,?)", (titulo, autor, year, isbn))
    conexion.commit()
    conexion.close()

def visualizar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo, autor, year, isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn=?", (titulo, autor, year, isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(ide):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (ide,))
    conexion.commit()
    conexion.close()

def actualizar(titulo, autor, year, isbn, ide):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, isbn=? WHERE id=?", (titulo, autor, year, isbn, ide))
    conexion.commit()
    conexion.close()






# Pruebas
conectar()
