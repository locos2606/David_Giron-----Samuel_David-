import unittest
from carroceria import Carroceria, TipoCarroceria

class TestCarroceria(unittest.TestCase):
    def test_init(self):
        carroceria = Carroceria(TipoCarroceria.Tubular, "rojo")
        self.assertEqual(carroceria.tipo, TipoCarroceria.Tubular)
        self.assertEqual(carroceria.color, "rojo")
    
    def test_str(self):
        carroceria = Carroceria(TipoCarroceria.Tubular, "rojo")
        self.assertEqual(str(carroceria), "Carroceria: Tubular, Color: rojo")

if __name__ == '__main__':
    unittest.main()
