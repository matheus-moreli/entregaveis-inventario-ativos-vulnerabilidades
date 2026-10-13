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
assert all((not (p and q)) == ((not p) or (not q))
           for p, q in product([False, True], repeat=2))
assert all(p or not p for p in (False, True))
assert not any(p and not p for p in (False, True))
contraexemplo = (False, True)
assert implicacao(*contraexemplo) and contraexemplo[1] and not contraexemplo[0]
print("Afirmação do consequente inválida: p=F, q=V é contraexemplo.")
