import numpy as np


# Linhas: equipamentos. Colunas: vulnerabilidades registradas.
matriz_incidencia = np.array(
    [
        [1, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
    ],
    dtype=float,
)
severidades = np.array([9.0, 7.5, 4.0])
risco_proprio = matriz_incidencia @ severidades

print("M =", matriz_incidencia)
print("v =", severidades)
print("b = Mv =", risco_proprio)
print("Ativo 1: 9.0; ativo 2: 11.5; ativo 3: 0.0.")
