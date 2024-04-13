class Motor:
    def __init__(self, volumen_litros):
        self.volumen_litros = volumen_litros

    def __str__(self):
        return f"Motor: {self.volumen_litros} litros"
