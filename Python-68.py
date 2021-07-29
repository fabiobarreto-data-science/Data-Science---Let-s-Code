"""
Enunciado
Desafio 3 - A sequência Fibonacci é a sequência cujos dois primeiros termos são 1 e os demais são obtidos através da soma de seus dois antecessores, isso é:

a. Fibonacci(1) = 1 e Fibonacci(2) = 2;

b. dado qualquer número n >= 3, Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

Assim, os 10 primeiros termos da sequência Fibonacci são:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
Faça uma função que receba um número n e calcule o termo de número n da sequência Fibonacci.
"""


def fibonacci(n):
    anterior, proximo = 1, 1
    temp = 0
    for c in range(n):
        print(anterior, end=', ')
        temp = anterior
        anterior = proximo
        proximo = temp + anterior


n = int(input("Que termo deseja encontrar: "))
fibonacci(n)