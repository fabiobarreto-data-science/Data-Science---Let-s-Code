"""
2. Classe Quadrado: Crie uma classe que modele um quadrado:

a) Atributos: Tamanho do lado
b) Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""


class Quadrado(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudarLado(self, tamanho):
        self.tamanho = tamanho

    def retornarValor(self):
        print(f"O novo valor do lado é {self.tamanho}")

    def CalcularArea(self):
        print(f"A área será {self.tamanho**2} m²")


quad = Quadrado(20)
print(quad.tamanho)
quad.mudarLado(40)
print(quad.tamanho)
quad.retornarValor()
quad.CalcularArea()