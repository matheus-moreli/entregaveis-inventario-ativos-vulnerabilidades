from collections import deque

grafo = {1: [2, 3], 2: [4], 3: [], 4: []}

def bfs(inicio):
    fila, vistos = deque([inicio]), {inicio}
    ordem = []
    while fila:
        atual = fila.popleft()
        ordem.append(atual)
        for vizinho in grafo[atual]:
            if vizinho not in vistos:
                vistos.add(vizinho)
                fila.append(vizinho)
    return ordem

def dfs(atual, vistos=None):
    vistos = set() if vistos is None else vistos
    vistos.add(atual)
    for vizinho in grafo[atual]:
        if vizinho not in vistos:
            dfs(vizinho, vistos)
    return vistos

print(bfs(1))
print(sorted(dfs(1)))
