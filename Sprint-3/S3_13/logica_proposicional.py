from itertools import product


def implicacao(p, q):
    return not p or q


print("p     q     p -> q     não(p e q)     não p ou não q")
for p, q in product([False, True], repeat=2):
    de_morgan_esquerda = not (p and q)
    de_morgan_direita = not p or not q
    print(p, q, implicacao(p, q), de_morgan_esquerda, de_morgan_direita)

print("As duas últimas colunas são iguais: Lei de De Morgan.")
print("Modus ponens: se p -> q e p são verdadeiros, então q é válido.")
