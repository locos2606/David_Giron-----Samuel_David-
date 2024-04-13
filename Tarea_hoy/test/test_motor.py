import unittest
from motor import Motor

class TestMotor(unittest.TestCase):
    def test_init(self):
        motor = Motor(2.0)
        self.assertEqual(motor.volumen_litros, 2.0)
    
    def test_str(self):
        motor = Motor(2.0)
        self.assertEqual(str(motor), "Motor: 2.0 litros")

if __name__ == '__main__':
    unittest.main()
