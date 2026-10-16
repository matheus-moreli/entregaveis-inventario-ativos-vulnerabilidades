import numpy as np


invertivel = np.array([[1.0, -0.2], [-0.3, 1.0]])
pesos_singulares = np.array(
    [[0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0]])
singular = np.eye(3) - pesos_singulares

for nome, matriz in [("invertível", invertivel), ("singular", singular)]:
    determinante = np.linalg.det(matriz)
    print(nome, "determinante =", determinante)
    if abs(determinante) < 1e-10:
        print("I - A é singular: não existe solução única.")
    else:
        print("Inversa =", np.linalg.inv(matriz))

exemplo_2x2 = np.array([[2.0, 1.0], [1.0, 1.0]])
exemplo_3x3 = np.array([[1.0, 2.0, 0.0], [0.0, 1.0, 1.0], [1.0, 0.0, 1.0]])
print("Inversa de [[2,1],[1,1]] =", np.linalg.inv(exemplo_2x2))
print("Determinante 3x3 por conferência =", np.linalg.det(exemplo_3x3))
