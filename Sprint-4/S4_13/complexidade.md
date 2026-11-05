# Complexidade usada no trabalho

| Operação | Ordem | Motivo |
|---|---:|---|
| Buscar ID no dicionário | O(1) médio | acesso por chave hash |
| Listar ou filtrar ativos | O(n) | examina os registros |
| Ordenar lista | O(n log n) | algoritmo interno de `sorted` |
| Eliminação de Gauss | O(n³) | pivôs, linhas e colunas |

A base acadêmica é pequena. A prioridade é manter o código verificável e escolher o dicionário onde ele melhora a busca.
