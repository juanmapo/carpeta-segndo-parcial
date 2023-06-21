import sqlite3
import pygame

def crear_tabla_puntuaciones():
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            sentencia = '''CREATE TABLE puntuaciones 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                score INTEGER
            )
            '''
            conexion.execute(sentencia)
            print("Se creó la tabla de puntuaciones")
        except sqlite3.OperationalError:
            print("La tabla de puntuaciones ya existe")
        except:
            print("Error al crear la tabla")

def leer_tabla_puntuaciones():
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.execute("SELECT nombre, score FROM puntuaciones ORDER BY score DESC LIMIT 10")
        resultados = cursor.fetchall()
    return resultados

def modificar_tabla_puntuaciones(nombre, score):
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            conexion.execute("INSERT INTO puntuaciones (nombre, score) VALUES (?, ?)", (nombre, score))
            conexion.commit()
            print("Se insertó el registro en la tabla de puntuaciones")
        except:
            print("Fallo al modificar la tabla de puntuaciones")







