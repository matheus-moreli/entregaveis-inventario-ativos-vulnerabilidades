def quick_sort(valores):
    if len(valores) <= 1:
        return valores
    pivo = valores[len(valores) // 2]
    menores = [v for v in valores if v < pivo]
    iguais = [v for v in valores if v == pivo]
    maiores = [v for v in valores if v > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

print(quick_sort([8, 3, 5, 1, 3]))
