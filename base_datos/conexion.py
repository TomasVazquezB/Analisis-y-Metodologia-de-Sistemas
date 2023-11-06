import sqlite3


class Conexion:

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
            KEY AUTOINCREMENT,nombre_mascota TEXT,raza_mascota TEXT,edad 
            INTEGER,cuidador_id 
            INTEGER,FOREIGN KEY (cuidador_id) REFERENCES cuidador(cuidador_id)""") 
   self.conn.commit()
  
  def create_cuidador_table(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS cuidador(cuidador_id INTEGER PRIMARY 
    KEY AUTOINCREMENT,nombre_cuidador TEXT, contrasena_cuidador TEXT,direccion_cuidador 
    TEXT)""")
    self.conn.commit()

  def insert_dueno(self,nombre_dueno,contrasena_dueno):
    self.cursor.execute("""INSERT INTO dueño(nombre_dueño,contrasena_dueno) VALUES 
    (?,?)""",(nombre_dueno,contrasena_dueno))
    self.conn.commit()

  def insert_mascota(self,nombre_mascota,tipo_mascota,edad):
   self.cursor.execute("""INSERT INTO mascota(nombre_mascota,raza_mascota,edad) VALUES 
   (?,?,?)""",(nombre_mascota,tipo_mascota,edad))
   self.conn.commit()

   def insert_cuidador(self,nombre_cuidador,contrasena_cuidador,direccion_cuidador):
    self.cursor.execute("""INSERT INTO cuidador(nombre_cuidador,contrasena_cuidador 
    ,direccion_cuidador) VALUES (?,?,?)""",
    (nombre_cuidador,contrasena_cuidador,direccion_cuidador))
    self.conn.commit()

  def close(self):
    self.conn.close()
    self.cursor.close()
