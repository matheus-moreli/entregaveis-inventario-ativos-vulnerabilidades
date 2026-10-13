def busca_binaria(valores, procurado):
    inicio, fim = 0, len(valores) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valores[meio] == procurado:
            return meio
        if valores[meio] < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


def bubble_sort(valores):
    resultado = valores[:]
    for limite in range(len(resultado) - 1, 0, -1):
        for indice in range(limite):
            if resultado[indice] > resultado[indice + 1]:
                resultado[indice], resultado[indice + 1] = resultado[indice + 1], resultado[indice]
    return resultado


def selection_sort(valores):
    resultado = valores[:]
    for inicio in range(len(resultado)):
        menor = inicio
        for indice in range(inicio + 1, len(resultado)):
            if resultado[indice] < resultado[menor]:
                menor = indice
        resultado[inicio], resultado[menor] = resultado[menor], resultado[inicio]
    return resultado


def insertion_sort(valores):
    resultado = valores[:]
    for indice in range(1, len(resultado)):
        chave = resultado[indice]
        anterior = indice - 1
        while anterior >= 0 and resultado[anterior] > chave:
            resultado[anterior + 1] = resultado[anterior]
            anterior -= 1
        resultado[anterior + 1] = chave
    return resultado


numeros = [42, 7, 19, 3, 28, 11]
ordenados = bubble_sort(numeros)
print("Bubble:", ordenados)
print("Selection:", selection_sort(numeros))
print("Insertion:", insertion_sort(numeros))
print("Busca binária de 19:", busca_binaria(ordenados, 19))
print("Busca binária O(log n), desde que a lista esteja ordenada.")
print("Bubble, Selection e Insertion: O(n²) no pior caso.")
