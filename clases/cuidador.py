import sqlite3


class Cuidador:

  def __init__(self):
    self.conn = sqlite3.connect("petpals.db")
    self.cursor = self.conn.cursor()

    def registrar_cuidador(self, nombre_cuidador: str, contrasena_cuidador: str, direccion_cuidador: str):self.conn.execute("INSERT INTO cuidador(nombre_cuidador, contrasena_cuidador, direccion_cuidador) VALUES(?, ?, ?)", (nombre_cuidador, contrasena_cuidador, direccion_cuidador))

  def consultar_cuidadores(self):
    query = "SELECT nombre_cuidador,direccion_cuidador FROM cuidador"
    self.conn.cursor.execute(query)
    cuidadores = self.conn.cursor.fetchall()
    return cuidadores
