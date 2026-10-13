# S3_04 — comparação de complexidade

| Algoritmo | Melhor caso | Caso médio | Pior caso | Escolha |
|---|---:|---:|---:|---|
| Busca linear | O(1) | O(n) | O(n) | lista sem ordenação |
| Busca binária | O(1) | O(log n) | O(log n) | lista ordenada |
| Bubble sort | O(n) | O(n²) | O(n²) | exemplo didático |
| Insertion sort | O(n) | O(n²) | O(n²) | poucos itens quase ordenados |

Para encontrar um ativo pelo ID numa lista já ordenada, a busca binária compara o
meio da lista e descarta metade a cada passo. Por isso é uma escolha melhor que
percorrer todos os itens quando a ordenação já existe. Não é adotada no CRUD JSON
principal porque o programa trabalha com poucos registros e prioriza leitura simples.
