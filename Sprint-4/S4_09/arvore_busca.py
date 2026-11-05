def inserir(no, valor):
    if no is None:
        return [valor, None, None]
    lado = 1 if valor < no[0] else 2
    no[lado] = inserir(no[lado], valor)
    return no

def em_ordem(no):
    return [] if no is None else em_ordem(no[1]) + [no[0]] + em_ordem(no[2])

raiz = None
for item in [5, 2, 8, 1, 3]:
    raiz = inserir(raiz, item)
print(em_ordem(raiz))
