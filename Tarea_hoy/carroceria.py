from enum import Enum

class TipoCarroceria(Enum):
    Independiente = 1
    Autoportante = 2
    Tubular = 3

class Carroceria:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def __str__(self):
        return f"Carroceria: {self.tipo.name}, Color: {self.color}"

