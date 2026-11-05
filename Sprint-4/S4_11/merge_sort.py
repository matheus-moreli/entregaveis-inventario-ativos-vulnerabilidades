def merge_sort(valores):
    if len(valores) <= 1:
        return valores
    meio = len(valores) // 2
    esquerda = merge_sort(valores[:meio])
    direita = merge_sort(valores[meio:])
    resultado = []
    while esquerda and direita:
        resultado.append((esquerda if esquerda[0] <= direita[0] else direita).pop(0))
    return resultado + esquerda + direita

print(merge_sort([8, 3, 5, 1]))
