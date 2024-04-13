import unittest
from carro import Carro
from motor import Motor
from chasis import Chasis, TipoChasis
from carroceria import Carroceria, TipoCarroceria
from llanta import Llanta
from asiento import Asiento

class TestCarro(unittest.TestCase):
    def setUp(self):
        self.motor = Motor(2.0)
        self.chasis = Chasis(TipoChasis.Monocasco)
        self.carroceria = Carroceria(TipoCarroceria.Tubular, "rojo")
        self.llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]
        self.asientos = [Asiento("Cuero", True) for _ in range(3)]
        self.carro = Carro(self.motor, self.chasis, self.carroceria, self.llantas, self.asientos)
    
    def test_str(self):
        detalles_llantas = '\n'.join([str(llanta) for llanta in self.llantas])
        detalles_asientos = '\n'.join([str(asiento) for asiento en self.asientos])
        expected_output = f"Carro:\n{self.motor}\n{self.chasis}\n{self.carroceria}\n{detalles_llantas}\n{detalles_asientos}"
        self.assertEqual(str(self.carro), expected_output)

if __name__ == '__main__':
    unittest.main()
