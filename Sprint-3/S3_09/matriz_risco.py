import numpy as np


# Linhas: equipamentos. Colunas: vulnerabilidades registradas.
matriz_incidencia = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
    ],
    dtype=float,
)
severidades = np.array([9.0, 7.5, 4.0, 2.0])
risco_proprio = matriz_incidencia @ severidades

print("M =", matriz_incidencia)
print("v =", severidades)
print("b = Mv =", risco_proprio)
print("posto =", np.linalg.matrix_rank(matriz_incidencia))
print("Núcleo: gerado por (0, 1, -1, 0).")
dependencias = np.array([[0, 0, 0], [0.25, 0, 0], [0, 0.5, 0]])
efetivo = np.linalg.solve(np.eye(3) - dependencias, risco_proprio)
print("Risco efetivo =", efetivo)
