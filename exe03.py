"""
3. Classe Retangulo: Crie uma classe que modele um retangulo:

a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b) Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

"""


class Retangulo(object):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarLados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def retornarLados(self):
        return self.comprimento, self.largura

    def area(self):
        area = self.largura * self.comprimento
        return area

    def perimetro(self):
        perimetro = self.largura*2 + self.comprimento*2
        print(f"A quantidade de rodapés será de {perimetro:.2f} metros")


comp = float(input("Qual o comprimento total do rodapé? (metros)"))
larg = float(input("Qual a dimensão do lado de cada piso? (m²)"))

