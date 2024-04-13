class Llanta:
    def __init__(self, marca, diametro_rin, altura, anchura):
        self.marca = marca
        self.diametro_rin = diametro_rin
        self.altura = altura
        self.anchura = anchura

    def __str__(self):
        return f"Llanta: Marca: {self.marca}, Rin: {self.diametro_rin}\", Altura: {self.altura}\", Anchura: {self.anchura}\""
