# S3_10 — eliminação de Gauss e interpretação

Para dois ativos, `B=[[2,1],[1,-1]]` e `b=(5,1)`. A matriz aumentada começa em `[2 1 | 5; 1 -1 | 1]`. Usando `R2 ← 2R2−R1`, obtém-se `[2 1 | 5; 0 -3 | -3]`. Substituição: `y=1` e `x=2`. `det(B)=-3≠0`, logo há solução única. Geometricamente, as duas equações são retas que se cruzam em `(2,1)`.

Para três ativos, tome `B=[[1,1,1],[2,-1,1],[1,2,-1]]` e `b=(6,3,2)`. A matriz aumentada é:

```text
[1  1  1 | 6]
[2 -1  1 | 3]
[1  2 -1 | 2]
```

`R2←R2−2R1` e `R3←R3−R1` dão `[0,-3,-1|-9]` e `[0,1,-2|-4]`. Então `R3←R3+(1/3)R2` dá `[0,0,-7/3|-7]`. Por substituição retroativa: `z=3`, `y=2`, `x=1`. Conferência: `B(1,2,3)=(6,3,2)`. Três planos se encontram em um ponto.

Classificação: se uma linha reduzida é `[0,0|c]` com `c≠0`, o sistema é impossível (retas paralelas distintas ou planos sem interseção comum). Se vira `[0,0|0]` e restam variáveis livres, há infinitas soluções (retas coincidentes ou planos com interseção em reta/plano). Exemplo 2×2: `[1,1|2;2,2|5]` vira `[0,0|1]`, impossível; trocando 5 por 4 vira `[0,0|0]`, infinito.

No inventário, a matriz é `I-A`, o termo independente é o risco próprio `Mv` e a incógnita é risco efetivo. Exemplo triangular: `I-A=[[1,0,0],[-0.25,1,0],[0,-0.5,1]]` e `b=(4,6,0)` dão `(4,7,3,5)`. A verificação `(I-A)r=b` é obrigatória; matriz não invertível produz erro explícito no código principal.
