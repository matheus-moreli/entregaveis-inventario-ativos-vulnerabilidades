"""Recursão e funções de alta ordem aplicadas à lista de ativos."""

from functools import reduce


def fatorial_iterativo(numero):
    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


def fatorial_recursivo(numero):
    if numero <= 1:
        return 1
    return numero * fatorial_recursivo(numero - 1)


def fibonacci_sem_memoria(numero):
    if numero <= 1:
        return numero
    return fibonacci_sem_memoria(numero - 1) + fibonacci_sem_memoria(numero - 2)


def fibonacci(numero, memoria=None):
    if memoria is None:
        memoria = {}
    if numero in memoria:
        return memoria[numero]
    if numero <= 1:
        return numero
    memoria[numero] = fibonacci(numero - 1, memoria) + fibonacci(numero - 2, memoria)
    return memoria[numero]


if __name__ == "__main__":
    ativos = [
        {"nome": "Notebook", "criticidade": "Média"},
        {"nome": "Servidor", "criticidade": "Alta"},
        {"nome": "Roteador", "criticidade": "Crítica"},
    ]
    nomes = list(map(lambda ativo: ativo["nome"], ativos))
    prioritarios = list(filter(
        lambda ativo: ativo["criticidade"] in ("Alta", "Crítica"), ativos))
    quantidade_letras = reduce(lambda total, nome: total + len(nome), nomes, 0)
    ordenados = sorted(ativos, key=lambda ativo: ativo["nome"])
    print("Fatorial:", fatorial_iterativo(12), fatorial_recursivo(12))
    print("Fibonacci com/sem memoização:", fibonacci(20), fibonacci_sem_memoria(20))
    print("Nomes com map:", nomes)
    print("Ativos prioritários com filter:", prioritarios)
    print("Total de letras com reduce:", quantidade_letras)
    print("Ordenados com lambda:", [ativo["nome"] for ativo in ordenados])
