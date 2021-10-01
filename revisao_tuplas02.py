import numpy as np
import statistics as st
"""
Enunciado
Crie uma função que recebe uma lista de números e devolve, nesta ordem, o mínimo, a média, o desvio padrão e o máximo.

Dica: Use a biblioteca statistics (import statistics) para calcular o desvio padrão: desvio = statistics.stdev(lista)
"""

lista = [6, 4, 3, 7, 8, 2, 9, 1]


def recebe_lista(lista):
    print(f"Valor mínimo: {min(lista)}")
    print(f"Valor médio: {np.mean(lista)}")
    print(f"Desvio padrão: {st.stdev(lista):.2f}")
    print(f"Valor máximo: {max(lista)}")


recebe_lista(lista)