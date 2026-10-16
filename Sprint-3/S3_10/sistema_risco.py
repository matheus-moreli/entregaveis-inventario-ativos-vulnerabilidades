import numpy as np


# A[i, j] indica quanto o ativo i depende do ativo j.
dependencias = np.array(
    [
        [0.0, 0.0, 0.0],
        [0.25, 0.0, 0.0],
        [0.0, 0.50, 0.0],
    ]
)
risco_proprio = np.array([4.0, 6.0, 0.0])
sistema = np.eye(3) - dependencias
risco_efetivo = np.linalg.solve(sistema, risco_proprio)

print("I - A =", sistema)
print("b =", risco_proprio)
print("x =", risco_efetivo)
print("Verificação:", sistema @ risco_efetivo)

# Segundo exemplo: eliminação de Gauss 2x2 com solução única.
dois = np.array([[2.0, 1.0], [1.0, -1.0]])
termos = np.array([5.0, 1.0])
print("Sistema 2x2:", np.linalg.solve(dois, termos))

# Terceiro exemplo: três planos com interseção em (1, 2, 3).
tres = np.array([[1.0, 1.0, 1.0], [2.0, -1.0, 1.0], [1.0, 2.0, -1.0]])
print("Sistema 3x3:", np.linalg.solve(tres, [6.0, 3.0, 2.0]))
