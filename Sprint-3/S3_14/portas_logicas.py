"""Tabelas de portas e circuito combinacional de autorização."""

from itertools import product


def portas(a, b):
    return (a and b, a or b, not (a and b), not (a or b),
            a != b, a == b)


def autorizar(credencial, permissao, bloqueado):
    return credencial and permissao and not bloqueado


if __name__ == "__main__":
    print("A B AND OR NAND NOR XOR XNOR")
    for a, b in product((False, True), repeat=2):
        print(int(a), int(b), *(int(valor) for valor in portas(a, b)))
    print("credencial permissao bloqueado autorizacao")
    for c, p, b in product((False, True), repeat=3):
        print(int(c), int(p), int(b), int(autorizar(c, p, b)))
    assert all((a and (a or b)) == a
               for a, b in product((False, True), repeat=2))
    print("Absorção A AND (A OR B) = A verificada.")
