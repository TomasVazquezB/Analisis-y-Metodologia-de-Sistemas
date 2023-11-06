import unittest
from main import Conexion


class TestConexion(unittest.TestCase):

    def setUp(self):
        self.conexion = Conexion()

    def test_validar_datos_dueno(self):
        data = {'nombre_dueno': 'Juan', 'direccion_dueno': 'Calle 123', 'mascota_id': 1}
        self.assertTrue(self.conexion.validar_datos(data, 'dueno'))

    def test_validar_datos_mascota(self):
        data = {'nombre_mascota': 'Firulais', 'raza_mascota': 'Labrador', 'edad': 5, 
        'cuidador_id': 1}
        self.assertTrue(self.conexion.validar_datos(data, 'mascota'))

    def test_validar_datos_cuidador(self):
        data = {'nombre_cuidador': 'Pedro', 'direccion_cuidador': 'Avenida 456'}
        self.assertTrue(self.conexion.validar_datos(data, 'cuidador'))

    def test_validar_datos_incorrecto(self):
        data = {'nombre': 'Pedro', 'direccion': 'Avenida 456'}
        self.assertFalse(self.conexion.validar_datos(data, 'dueno'))

if __name__ == '__main__':
    unittest.main()
