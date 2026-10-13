# S3_02 — recursão, memoização e funções de alta ordem

`algoritmos.py` implementa fatorial iterativo/recursivo e Fibonacci com/sem memoização. Fatorial usa caso-base `n≤1` e caso recursivo `n·f(n−1)`. Fibonacci usa casos-base 0/1 e soma os dois anteriores; sem cache repete subproblemas, com dicionário calcula cada `F(k)` uma vez. `map` extrai nomes de ativos, `filter` seleciona criticidade Alta/Crítica, `reduce` soma comprimento dos nomes e `sorted(..., key=lambda ...)` ordena os ativos.

Medição reproduzível: `python Sprint-3/S3_02/comparar_desempenho.py`, Python 3.13.15 no Windows. Cada número abaixo é a mediana de cinco medições. Fatorial usa 1000 chamadas por medição; Fibonacci usa uma, pois o caso sem cache fica caro. As funções produziram os mesmos valores em cada entrada.

| Cálculo | n | Abordagem 1 | ms/chamada | Abordagem 2 | ms/chamada |
|---|---:|---|---:|---|---:|
| Fatorial | 100 | iterativa | 0,002120 | recursiva | 0,003742 |
| Fatorial | 400 | iterativa | 0,018377 | recursiva | 0,035878 |
| Fatorial | 800 | iterativa | 0,074453 | recursiva | 0,114057 |
| Fibonacci | 10 | sem cache | 0,0047 | memoizada | 0,0012 |
| Fibonacci | 20 | sem cache | 0,5441 | memoizada | 0,0023 |
| Fibonacci | 30 | sem cache | 66,0056 | memoizada | 0,0037 |

Fatorial em ambas as versões faz O(n) multiplicações; a recursiva adiciona O(n) quadros de pilha e pode atingir o limite de recursão do Python. Fibonacci ingênuo tem chamadas repetidas em crescimento exponencial; memoizado é O(n) tempo e O(n) memória. Os tempos absolutos dependem da máquina e da carga do sistema; o contraste grande em `F(30)` é a evidência relevante. Para uma lista de ativos pequena, `map/filter/reduce` e compreensão/lista com laços podem ser escolhidos pela clareza; nenhuma dessas funções melhora automaticamente a complexidade.
