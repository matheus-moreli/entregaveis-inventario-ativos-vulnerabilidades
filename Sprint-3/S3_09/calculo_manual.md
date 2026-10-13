# S3_09 — multiplicação matriz-vetor

Foi usada a matriz de propagação:

M = [[1, 0, 0], [0, 1, 1], [0, 0, 0]]

e o vetor de severidades:

v = [9, 7,5, 4].

O produto é calculado linha a linha:

- linha 1: 1×9 + 0×7,5 + 0×4 = 9;
- linha 2: 0×9 + 1×7,5 + 1×4 = 11,5;
- linha 3: 0×9 + 0×7,5 + 0×4 = 0.

Logo, Mv = [9, 11,5, 0]. O segundo ativo recebe a influência da sua própria
severidade e de uma dependência. O arquivo matriz_risco.py reproduz o cálculo
com NumPy e imprime o mesmo resultado.
