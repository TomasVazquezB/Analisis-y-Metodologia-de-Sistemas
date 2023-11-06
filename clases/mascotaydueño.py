import sqlite3


class dueñoymascota:

  def __init__(self):
    self.conn = sqlite3.connect("petpals.db")
    self.cursor = self.conn.cursor()

  def registrar_dueno(self, nombre_dueno: str, direccion_dueno: str):
    self.conn.execute("INSERT INTO dueño(nombre_dueno, direccion_dueno) VALUES(?,?)",(nombre_dueno, direccion_dueno))

  def registrar_mascota(self, nombre_mascota: str, tipo_mascota: str,
  dueno_id: int, edad: int):
    self.conn.execute("INSERT INTO mascota(nombre_mascota,raza_mascota,edad,dueno_id) VALUES(?,?,?,?)",
(nombre_mascota, tipo_mascota, dueno_id, edad))

  def consultar_mascotas_por_dueño(self, dueno_id: int):
    query = "SELECT nombre_mascota,raza_mascota,edad FROM mascota WHERE dueno_id=?"
    self.conn.cursor.execute(query, (dueno_id))
    mascotas = self.conn.cursor.fetchall()
    return mascotas
