from enum import Enum

class TipoChasis(Enum):
    Independiente = 1
    Monocasco = 2

class Chasis:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Chasis: {self.tipo.name}"
