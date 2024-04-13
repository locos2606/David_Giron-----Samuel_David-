from carro import Carro
from motor import Motor
from chasis import Chasis, TipoChasis
from carroceria import Carroceria, TipoCarroceria
from llanta import Llanta
from asiento import Asiento

if __name__ == "__main__":
    motor = Motor(2.0)
    chasis = Chasis(TipoChasis.Monocasco)
    carroceria = Carroceria(TipoCarroceria.Tubular, "rojo")
    
    llantas = [
        Llanta("Goodyear", 25, 20, 15),
        Llanta("Goodyear", 25, 20, 15),
        Llanta("Goodyear", 25, 20, 15),
        Llanta("Goodyear", 25, 20, 15)
    ]

    asientos = [
        Asiento("Cuero", True),
        Asiento("Cuero", True),
        Asiento("Tela", False)
    ]

    carro = Carro(motor, chasis, carroceria, llantas, asientos)
    print(carro)
