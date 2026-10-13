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
