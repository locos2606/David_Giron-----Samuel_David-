import unittest
from llanta import Llanta

class TestLlanta(unittest.TestCase):
    def test_init(self):
        llanta = Llanta("Goodyear", 25, 20, 15)
        self.assertEqual(llanta.marca, "Goodyear")
        self.assertEqual(llanta.diametro_rin, 25)
        self.assertEqual(llanta.altura, 20)
        self.assertEqual(llanta.anchura, 15)
    
    def test_str(self):
        llanta = Llanta("Goodyear", 25, 20, 15)
        self.assertEqual(str(llanta), 'Llanta: Marca: Goodyear, Rin: 25", Altura: 20", Anchura: 15"')

if __name__ == '__main__':
    unittest.main()
