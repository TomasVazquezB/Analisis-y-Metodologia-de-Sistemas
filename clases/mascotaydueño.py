import sqlite3


class dueñoymascota:

  def __init__(self):
    self.conn = sqlite3.connect("petpals.db")
    self.cursor = self.conn.cursor()


  def create_dueno_table(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS dueño(dueno_id INTEGER PRIMARY KEY
    AUTOINCREMENT,nombre_dueno TEXT,contrasena_dueño TEXT,mascota_id
    INTEGER,FOREIGN KEY (mascota_id) REFERENCES mascota(mascota_id))""")
    self.conn.commit()

  def create_mascota_table(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS mascota(mascota_id INTEGER PRIMARY 
    KEY AUTOINCREMENT,nombre_mascota TEXT,raza_mascota TEXT,edad INTEGER,cuidador_id 
    INTEGER,FOREIGN KEY (cuidador_id) REFERENCES cuidador(cuidador_id))""")
    self.conn.commit()
  
  def registrar_dueno(self, nombre_dueno: str, contrasena_dueno: str):
    self.create_dueno_table()
    self.conn.execute("INSERT INTO dueño(nombre_dueno, contrasena_dueño) VALUES(?, ?)", (nombre_dueno, contrasena_dueno))
    self.conn.commit()

  
  def registrar_mascota(self, nombre_mascota: str, tipo_mascota: str, edad: int):
    self.create_mascota_table()
    self.conn.execute("INSERT INTO mascota(nombre_mascota,raza_mascota,edad) VALUES(?,?,?)",(nombre_mascota, tipo_mascota,edad))
    self.conn.commit()

  def consultar_mascotas_por_dueño(self, dueno_id: int):
    query = "SELECT nombre_mascota,raza_mascota,edad FROM mascota WHERE dueno_id=?"
    self.conn.cursor.execute(query, (dueno_id))
    mascotas = self.conn.cursor.fetchall()
    return mascotas
