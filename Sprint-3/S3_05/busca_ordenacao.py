def busca_binaria(valores, procurado, contar=False):
    inicio, fim = 0, len(valores) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if valores[meio] == procurado:
            return (meio, comparacoes) if contar else meio
        if valores[meio] < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return (-1, comparacoes) if contar else -1


def bubble_sort(valores, contar=False):
    resultado = valores[:]
    comparacoes = 0
    for limite in range(len(resultado) - 1, 0, -1):
        trocou = False
        for indice in range(limite):
            comparacoes += 1
            if resultado[indice] > resultado[indice + 1]:
                resultado[indice], resultado[indice + 1] = resultado[indice + 1], resultado[indice]
                trocou = True
        if not trocou:
            break
    return (resultado, comparacoes) if contar else resultado


def selection_sort(valores, contar=False):
    resultado = valores[:]
    comparacoes = 0
    for inicio in range(len(resultado)):
        menor = inicio
        for indice in range(inicio + 1, len(resultado)):
            comparacoes += 1
            if resultado[indice] < resultado[menor]:
                menor = indice
        resultado[inicio], resultado[menor] = resultado[menor], resultado[inicio]
    return (resultado, comparacoes) if contar else resultado


def insertion_sort(valores, contar=False):
    resultado = valores[:]
    comparacoes = 0
    for indice in range(1, len(resultado)):
        chave = resultado[indice]
        anterior = indice - 1
        while anterior >= 0:
            comparacoes += 1
            if resultado[anterior] <= chave:
                break
            resultado[anterior + 1] = resultado[anterior]
            anterior -= 1
        resultado[anterior + 1] = chave
    return (resultado, comparacoes) if contar else resultado


if __name__ == "__main__":
    ativos = ["SRV-WEB", "NB-LAB", "RT-FILIAL", "APP-PORTAL"]
    ordenados = bubble_sort(ativos)
    print("Ativos ordenados:", ordenados)
    print("Busca binária de NB-LAB:", busca_binaria(ordenados, "NB-LAB"))
