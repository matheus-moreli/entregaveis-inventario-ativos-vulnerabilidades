# S3_10 — sistema linear de risco

O programa resolve (I - A)x = b. Para o exemplo:

- I - A = [[1, 0, 0], [-0,25, 1, 0], [0, -0,5, 1]];
- b = [4, 6, 0].

Por substituição:

1. x1 = 4;
2. -0,25×4 + x2 = 6, então x2 = 7;
3. -0,5×7 + x3 = 0, então x3 = 3,5.

O resultado é x = [4, 7, 3,5]. A verificação do programa recalcula (I-A)x e
obtém [4, 6, 0], igual ao vetor b.
