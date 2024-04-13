class Asiento:
    def __init__(self, material, tiene_funda):
        self.material = material
        self.tiene_funda = tiene_funda

    def __str__(self):
        return f"Asiento: Material: {self.material}, Funda: {'Sí' if self.tiene_funda else 'No'}"
