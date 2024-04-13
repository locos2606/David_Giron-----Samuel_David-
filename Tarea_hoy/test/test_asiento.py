import unittest
from asiento import Asiento

class TestAsiento(unittest.TestCase):
    def test_init(self):
        asiento = Asiento("Cuero", True)
        self.assertEqual(asiento.material, "Cuero")
        self.assertTrue(asiento.tiene_funda)
    
    def test_str(self):
        asiento = Asiento("Cuero", True)
        self.assertEqual(str(asiento), "Asiento: Material: Cuero, Funda: Sí")

if __name__ == '__main__':
    unittest.main()
