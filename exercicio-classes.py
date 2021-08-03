"""
1. Classe Bola: Crie uma classe que modele uma bola:

a) Atributos: Cor, circunferência, material
b) Métodos: trocaCor e mostraCor

"""


class Bola(object):
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocaCor(self, tcor):
        self.cor = tcor

    def mostraCor(self):
        print(f"A cor é {self.cor}")


bola1 = Bola("Vermelho", 10, "Couro")
print(bola1.cor)
print(bola1.circuferencia)
print(bola1.material)
bola1.trocaCor("Azul")
bola1.mostraCor()