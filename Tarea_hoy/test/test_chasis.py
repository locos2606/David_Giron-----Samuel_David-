import unittest
from chasis import Chasis, TipoChasis

class TestChasis(unittest.TestCase):
    def test_init(self):
        chasis = Chasis(TipoChasis.Monocasco)
        self.assertEqual(chasis.tipo, TipoChasis.Monocasco)
    
    def test_str(self):
        chasis = Chasis(TipoChasis.Monocasco)
        self.assertEqual(str(chasis), "Chasis: Monocasco")

if __name__ == '__main__':
    unittest.main()
