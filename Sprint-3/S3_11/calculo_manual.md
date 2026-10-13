# S3_11 — invertibilidade

Para uma matriz 2×2 [[a, b], [c, d]], o determinante é ad - bc.

No exemplo invertível do código, o determinante calculado é 0,94. Como ele é
diferente de zero, existe inversa e o sistema tem solução única.

No exemplo singular, o determinante é 0. Isso significa que uma linha é combinação
da outra ou que a transformação perde informação. Por essa razão a inversa não
existe e não se deve chamar a função de inversão para esse caso.
