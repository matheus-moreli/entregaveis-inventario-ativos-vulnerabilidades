"""Medianas de cinco medições; o relatório registra a máquina e o método."""

import platform
from statistics import median
from timeit import repeat

from algoritmos import (fatorial_iterativo, fatorial_recursivo, fibonacci,
                        fibonacci_sem_memoria)


def medir(funcao, numero, repeticoes):
    tempos = repeat(lambda: funcao(numero), repeat=5, number=repeticoes)
    return median(tempos) * 1000 / repeticoes


print("Python", platform.python_version(), platform.system())
for tamanho in (100, 400, 800):
    assert fatorial_iterativo(tamanho) == fatorial_recursivo(tamanho)
    print("fatorial", tamanho,
          round(medir(fatorial_iterativo, tamanho, 1000), 6),
          round(medir(fatorial_recursivo, tamanho, 1000), 6), "ms/chamada")
for tamanho in (10, 20, 30):
    assert fibonacci_sem_memoria(tamanho) == fibonacci(tamanho)
    print("fibonacci", tamanho,
          round(medir(fibonacci_sem_memoria, tamanho, 1), 6),
          round(medir(fibonacci, tamanho, 1), 6), "ms/chamada")
