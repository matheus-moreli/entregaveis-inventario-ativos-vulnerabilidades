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

# Cenário do material de apoio: V2 afeta Web e Banco; V4 ainda não afeta ninguém.
matriz_aula = np.array([[1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]], dtype=float)
severidades_aula = np.array([9.8, 5.3, 7.5, 4.3])
proprio_aula = matriz_aula @ severidades_aula
dependencias_aula = np.array([[0.0, 0.2, 0.0], [0.5, 0.0, 0.0], [0.0, 0.6, 0.0]])
efetivo_aula = np.linalg.solve(np.eye(3) - dependencias_aula, proprio_aula)
fator_exemplo = np.diag([1.5, 1.0, 1.0])
print("M da aula =", matriz_aula)
print("b da aula =", proprio_aula)
print("x da aula =", np.round(efetivo_aula, 2))
print("Extensão opcional F(Mv) =", fator_exemplo @ proprio_aula)
