from functools import reduce
from time import perf_counter


def fatorial_iterativo(numero):
    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


def fatorial_recursivo(numero):
    if numero <= 1:
        return 1
    return numero * fatorial_recursivo(numero - 1)


def fibonacci(numero, memoria=None):
    if memoria is None:
        memoria = {}
    if numero in memoria:
        return memoria[numero]
    if numero <= 1:
        return numero
    memoria[numero] = fibonacci(numero - 1, memoria) + fibonacci(numero - 2, memoria)
    return memoria[numero]


ativos = [
    {"nome": "Notebook", "criticidade": "Média"},
    {"nome": "Servidor", "criticidade": "Alta"},
    {"nome": "Roteador", "criticidade": "Crítica"},
]
nomes = list(map(lambda ativo: ativo["nome"], ativos))
prioritarios = list(filter(lambda ativo: ativo["criticidade"] in ["Alta", "Crítica"], ativos))
quantidade_letras = reduce(lambda total, nome: total + len(nome), nomes, 0)

inicio = perf_counter()
iterativo = fatorial_iterativo(12)
tempo_iterativo = perf_counter() - inicio
inicio = perf_counter()
recursivo = fatorial_recursivo(12)
tempo_recursivo = perf_counter() - inicio

print("Fatorial iterativo:", iterativo, "em", tempo_iterativo)
print("Fatorial recursivo:", recursivo, "em", tempo_recursivo)
print("Fibonacci com memoização:", fibonacci(30))
print("Nomes com map:", nomes)
print("Ativos prioritários com filter:", prioritarios)
print("Total de letras com reduce:", quantidade_letras)
