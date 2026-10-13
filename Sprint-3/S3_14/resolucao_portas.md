# S3_14 — portas lógicas

| P | Q | AND | OR | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

Uma condição de acesso pode ser modelada por AND: o usuário precisa possuir
credencial válida **e** permissão. OR representa alternativas válidas, enquanto XOR
é verdadeiro apenas quando exatamente uma entrada é verdadeira. O arquivo
portas_logicas.py gera essas combinações de forma programática.
