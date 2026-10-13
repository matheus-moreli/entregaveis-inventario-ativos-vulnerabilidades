import numpy as np


valor = 0.1 + 0.2
esperado = 0.3
erro_absoluto = abs(valor - esperado)
erro_relativo = erro_absoluto / abs(esperado)
print("0.1 + 0.2 =", repr(valor))
print("Erro absoluto:", erro_absoluto)
print("Erro relativo:", erro_relativo)
print("Comparação com tolerância:", np.isclose(valor, esperado, atol=1e-12))

matriz = np.array([[1.0, 0.999999], [0.999999, 0.999998]])
vetor = np.array([2.0, 1.999997])
print("Número de condição:", np.linalg.cond(matriz))
try:
    direto = np.linalg.solve(matriz, vetor)
    por_inversa = np.linalg.inv(matriz) @ vetor
    print("solve:", direto)
    print("inv @ b:", por_inversa)
except np.linalg.LinAlgError:
    print("Matriz singular ou numericamente instável.")
