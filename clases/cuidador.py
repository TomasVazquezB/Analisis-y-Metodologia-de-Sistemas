import sqlite3

class Cuidador:
  def __init__(self):
    self.conn = sqlite3.connect("petpals.db")
    self.cursor = self.conn.cursor()

  def create_cuidador_table(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS cuidador(cuidador_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_cuidador TEXT, contrasena_cuidador TEXT, direccion_cuidador TEXT)""")
    self.conn.commit()

  def registrar_cuidador(self, nombre_cuidador: str, contrasena_cuidador: str, direccion_cuidador: str):
    self.create_cuidador_table()
    self.conn.execute("INSERT INTO cuidador(nombre_cuidador, contrasena_cuidador, direccion_cuidador) VALUES(?, ?, ?)",
      (nombre_cuidador, contrasena_cuidador, direccion_cuidador))
    self.conn.commit()

  def consultar_cuidadores(self):
    query = "SELECT nombre_cuidador, direccion_cuidador FROM cuidador"
    self.conn.cursor.execute(query)
    cuidadores = self.conn.cursor.fetchall()
    return cuidadores
