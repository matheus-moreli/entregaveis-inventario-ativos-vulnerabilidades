# S3_05 — busca e ordenação de ativos

`busca_ordenacao.py` implementa busca binária, Bubble, Selection e Insertion. `comparar.py` usa sequências de tamanho 20, 100 e 300, ordenadas, invertidas e embaralhadas com semente 42; conta comparações de elementos (não mede tempo de máquina). As três ordenações produzem o mesmo resultado que `sorted`. A busca procura o último elemento da lista já ordenada.

| n | Entrada | Bubble | Selection | Insertion | Busca binária |
|---:|---|---:|---:|---:|---:|
| 20 | ordenada | 19 | 190 | 19 | 5 |
| 20 | inversa | 190 | 190 | 190 | 5 |
| 20 | aleatória | 190 | 190 | 137 | 5 |
| 100 | ordenada | 99 | 4950 | 99 | 7 |
| 100 | inversa | 4950 | 4950 | 4950 | 7 |
| 100 | aleatória | 4940 | 4950 | 2597 | 7 |
| 300 | ordenada | 299 | 44850 | 299 | 9 |
| 300 | inversa | 44850 | 44850 | 44850 | 9 |
| 300 | aleatória | 44772 | 44850 | 24468 | 9 |

Bubble usa parada antecipada e por isso é O(n) no melhor caso e O(n²) no pior. Selection compara sempre `n(n−1)/2` pares, logo O(n²) mesmo já ordenado. Insertion é O(n) ordenado e O(n²) no pior caso; costuma ser simples e útil para listas pequenas ou quase ordenadas. Bubble e Insertion preservam a ordem de itens iguais; Selection com troca direta pode não preservar. As três usam memória auxiliar O(n) nesta implementação porque copiam a lista de entrada; o núcleo da ordenação usa O(1) extra.

Busca binária é O(log n) comparações, mas **exige lista ordenada pela mesma chave**. Usá-la sobre nomes de ativos em ordem de cadastro pode retornar ausência falsa. Para uma única consulta em lista desordenada, a busca linear O(n) pode custar menos que ordenar tudo antes. Para consultas repetidas, ordenar uma vez pode compensar; no CRUD principal, ID já é chave de dicionário, então a consulta direta é mais apropriada que busca binária.

Reprodução: `python Sprint-3/S3_05/comparar.py`. Os números acima são contagens da execução, não valores teóricos inventados.
