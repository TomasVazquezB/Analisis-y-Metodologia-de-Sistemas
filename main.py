from flask import Flask, redirect, request
from flask.helpers import url_for
from flask.templating import render_template
from clases.cuidador import Cuidador
from clases.mascotaydueño import dueñoymascota
import sqlite3


def __init__(self):
    self.conn = sqlite3.connect("petpals.db")
    self.cursor = self.conn.cursor()
   
class Conexion:
  def validar_datos(self, data, tipo):
   if tipo == 'dueno':
     if 'nombre_dueno' not in data or 'direccion_dueno' not in data or 'mascota_id' not in data:
       return False

   elif tipo == 'mascota':
    if 'nombre_mascota' not in data or 'raza_mascota' not in data or 'edad' not in data or 'cuidador_id' not in data:
      return False
  
   elif tipo == 'cuidador':
      if 'nombre_cuidador' not in data or 'direccion_cuidador' not in data:
       return False

   else:
     return True

   def close(self):
    self.conn.commit()
    self.conn.close()

  def get_json(data):
   return request.get_json()

  def generar_respuesta(mensaje):
    return {'message': mensaje}
     
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        dueño_mascota = dueñoymascota()
        #usuario = request.form["usuario"]
        usuario = request.form.get("usuario", "")
        #contrasena = request.form["contrasena"]
        contrasena = request.form.get("contrasena", "")
        #nombre_mascota = request.form["nombre_mascota"]
        nombre_mascota = request.form.get("nombre_mascota", "")  
        #raza = request.form["raza"]
        raza = request.form.get("raza", "")
        #edad = request.form["edad"]
        edad = request.form.get("edad", "")

        dueño_mascota.create_dueno_table()
        dueño_mascota.registrar_dueno(usuario, contrasena)
        dueño_mascota.registrar_mascota(nombre_mascota, raza, edad)
    
        return redirect(url_for('cuidador', usuario=usuario, contrasena=contrasena,nombre_mascota=nombre_mascota,
raza=raza, edad=edad))
    return render_template("index.html")
  
@app.route('/cuidador', methods=["GET","POST"])
def cuidador():
    if request.method == "POST":
        cuidador = Cuidador()
        usuario2 = request.form.get("usuario2","")
        contrasena2 = request.form.get("contrasena2","")
        direccion = request.form.get("direccion","")

        cuidador.registrar_cuidador(usuario2, contrasena2, direccion)

        return redirect(url_for('resultados', usuario2=usuario2, contrasena2=contrasena2,direccion=direccion))
    return render_template("cuidador.html")

@app.route('/resultados', methods=["GET","POST"])
def resultados():
    usuario = request.args.get('usuario')
    contrasena = request.args.get('contrasena')
    nombre_mascota = request.args.get('nombre_mascota')
    raza = request.args.get('raza')
    edad = request.args.get('edad') 
    usuario2 = request.args.get('usuario2')
    contrasena2 = request.args.get('contrasena2')
    direccion = request.args.get('direccion')

    return render_template("resultados.html",usuario=usuario, contrasena=contrasena,nombre_mascota=nombre_mascota,
raza=raza,edad=edad,usuario2=usuario2,contrasena2=contrasena2,direccion=direccion)
  
if __name__ == '__main__':  
 app.run(host='0.0.0.0', port=81, debug=True)

#data = get_json(request.data)
#if not conn.validar_datos(data, 'dueno'):
 #  return generar_respuesta('Los datos son inválidos')
#dueno = dueñoymascota(conn.conn)
#dueno.registrar_dueno(data['nombre'], data['contrasena'], data [] ])
#  conn.close()
#  return generar_respuesta('El Dueño fue registrado con éxito')


##  data = get_json(request.data)
##  conn = Conexion()
##  if not conn.validar_datos(data, 'mascota'):
##   return generar_respuesta('Los datos son inválidos')
##  mascota = dueñoymascota(conn.conn)
##  mascota.registrar_mascota(data['nombre'], data['raza'], data['edad'], data['dueño_id'])
##  conn.close()
##  return generar_respuesta('La Mascota fue registrada con éxito')

