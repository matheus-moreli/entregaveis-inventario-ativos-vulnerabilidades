"""Conta comparações com entradas reproduzíveis para o relatório S3_05."""

from random import Random

from busca_ordenacao import (bubble_sort, busca_binaria, insertion_sort,
                            selection_sort)


for tamanho in (20, 100, 300):
    aleatorios = list(range(tamanho))
    Random(42).shuffle(aleatorios)
    for nome, dados in (("ordenada", list(range(tamanho))),
                        ("inversa", list(range(tamanho - 1, -1, -1))),
                        ("aleatoria", aleatorios)):
        resultados = []
        for algoritmo in (bubble_sort, selection_sort, insertion_sort):
            ordenados, comparacoes = algoritmo(dados, contar=True)
            assert ordenados == list(range(tamanho))
            resultados.append(comparacoes)
        indice, busca = busca_binaria(ordenados, tamanho - 1, contar=True)
        assert indice == tamanho - 1
        print(tamanho, nome, *resultados, busca)
