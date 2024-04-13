from motor import Motor
from chasis import Chasis, TipoChasis
from carroceria import Carroceria, TipoCarroceria
from llanta import Llanta
from asiento import Asiento

class Carro:
    def __init__(self, motor, chasis, carroceria, llantas, asientos):
        self.motor = motor
        self.chasis = chasis
        self.carroceria = carroceria
        self.llantas = llantas
        self.asientos = asientos

    def __str__(self):
        detalles_llantas = '\n'.join([str(llanta) for llanta in self.llantas])
        detalles_asientos = '\n'.join([str(asiento) for asiento in self.asientos])
        return f"Carro:\n{self.motor}\n{self.chasis}\n{self.carroceria}\n{detalles_llantas}\n{detalles_asientos}"
