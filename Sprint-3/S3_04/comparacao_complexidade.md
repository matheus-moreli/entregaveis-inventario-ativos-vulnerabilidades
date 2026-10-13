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

## Justificativas e escala

- **O(1):** consultar uma posição conhecida de uma lista não percorre os demais itens; `dict[id]` tem busca média O(1), embora colisões possam piorar o caso extremo.
- **O(log n):** a busca binária reduz pela metade o espaço restante a cada comparação. Para 1.024 itens ordenados, precisa de no máximo cerca de 11 comparações.
- **O(n):** a busca linear pode percorrer todos os itens. No melhor caso, o alvo está na primeira posição.
- **O(n log n):** algoritmos eficientes de ordenação combinam uma quantidade logarítmica de etapas com processamento linear em cada etapa; o `sort()` do Python é uma escolha prática, sem precisar reimplementar ordenação no CRUD.
- **O(n²):** duas passagens aninhadas, como nos sorts didáticos acima, crescem rapidamente. Bubble Sort chega a O(n) no melhor caso apenas quando implementa parada antecipada; a versão de S3_05 faz isso.
- **O(2ⁿ):** a recursão ingênua de Fibonacci em S3_02 recalcula subproblemas; a versão com memoização elimina a repetição e cai para O(n).

Quando o volume dobra, O(n) tende a duplicar o trabalho e O(n²) tende a quadruplicá-lo. Big-O descreve crescimento, não tempo absoluto: custo de implementação, tamanho dos dados e constantes também influenciam a escolha. Na lista encadeada de S3_03, buscar ou inserir no fim sem ponteiro de cauda é O(n), enquanto anexar à lista Python é O(1) amortizado.
