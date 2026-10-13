# S3_13 — lista resolvida de lógica proposicional

Defina P = “o ativo existe” e Q = “a nota CVSS é válida”. A operação de cadastro exige `P∧Q`. A condicional `P→Q` equivale a `¬P∨Q`; ela só é falsa quando P é verdadeiro e Q é falso. A bicondicional é `(P→Q)∧(Q→P)`.

| P | Q | P∧Q | P∨Q | P→Q | P↔Q | ¬(P∧Q) | ¬P∨¬Q |
|---|---|---|---|---|---|---|---|
| F | F | F | F | V | V | V | V |
| F | V | F | V | V | F | V | V |
| V | F | F | V | F | F | V | V |
| V | V | V | V | V | V | F | F |

As duas últimas colunas provam por tabela a lei de De Morgan `¬(P∧Q)≡¬P∨¬Q`. A outra lei `¬(P∨Q)≡¬P∧¬Q` segue pelo mesmo raciocínio: só é verdadeira quando ambos são falsos. `P∨¬P` é tautologia, pois sempre V; `P∧¬P` é contradição, pois sempre F.

**Argumento válido (modus ponens):** premissas `P→Q` e P; conclusão Q. Se ambas as premissas são V, P=V e a condicional obriga Q=V. Não existe linha com premissas V e conclusão F. Aplicação: “se CVSS está fora da faixa, rejeita; CVSS está fora; logo rejeita”. **Argumento inválido (afirmação do consequente):** premissas `P→Q` e Q; conclusão P. Contraexemplo P=F, Q=V: a condicional e Q são V, mas P é F. Aplicação: “se há vulnerabilidade, o risco é positivo; risco positivo, logo há vulnerabilidade” é inválido, pois risco pode ser herdado por dependência.

**Regra de inferência adicional (modus tollens):** `P→Q`, `¬Q` implicam `¬P`; se P fosse V, Q teria de ser V, contradizendo `¬Q`. Em código, `if not ativo or not cvss_valido: rejeitar()` é a negação da conjunção exigida para cadastro. `logica_proposicional.py` imprime linhas para conferir De Morgan e implicação.
