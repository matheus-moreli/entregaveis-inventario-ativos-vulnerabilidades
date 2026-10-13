import numpy as np


invertivel = np.array([[1.0, -0.2], [-0.3, 1.0]])
singular = np.array([[1.0, -1.0], [-1.0, 1.0]])

for nome, matriz in [("invertível", invertivel), ("singular", singular)]:
    determinante = np.linalg.det(matriz)
    print(nome, "determinante =", determinante)
    if abs(determinante) < 1e-10:
        print("I - A é singular: não existe solução única.")
    else:
        print("Inversa =", np.linalg.inv(matriz))

print("Para matriz 3x3, a regra de Sarrus é uma forma manual possível.")
