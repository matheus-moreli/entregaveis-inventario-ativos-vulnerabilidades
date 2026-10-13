# S3_12 — erros numéricos

Computadores armazenam números reais em ponto flutuante, com quantidade finita de
bits. Por isso 0.1 + 0.2 aparece como 0.30000000000000004.

No exemplo:

- erro absoluto: valor obtido menos valor esperado, em módulo;
- erro relativo: erro absoluto dividido pelo valor esperado;
- comparação segura: usar tolerância, e não igualdade direta entre floats.

A matriz mal condicionada teve número de condição aproximado de
3.999.398.504.836,58. Isso explica por que pequenas alterações de entrada podem
produzir variações grandes. Para resolver sistemas, solve é preferível a calcular
a inversa e depois multiplicar.
