# S3_09 — transformação linear do risco

Três equipamentos (E1 notebook, E2 servidor, E3 roteador) e quatro ocorrências de vulnerabilidade (V1–V4). A matriz de incidência tem linhas de equipamentos e colunas de ocorrências:

```text
M = [1 0 0 0]
    [0 1 1 0]
    [0 0 0 1]       v = [9; 7,5; 4; 2]
```

`T(v)=Mv` é transformação linear de R⁴ em R³: `T(u+w)=T(u)+T(w)` e `T(cu)=cT(u)` pela distributividade do produto matricial. O domínio tem dimensão 4, o contradomínio 3. Linha a linha: `p1=9`, `p2=7,5+4=11,5`, `p3=2`; logo `p=(9;11,5;2)` é o risco próprio. **M não contém dependências entre ativos**; isso fica em A.

As três linhas são independentes, então posto(M)=3 e imagem(T)=R³. O núcleo resolve `v1=0`, `v2+v3=0`, `v4=0`, portanto `ker(T)=span{(0,1,-1,0)}` e dimensão 1. Confere posto+nulidade=3+1=4. Geometricamente, aumentar V2 e diminuir V3 no mesmo valor não altera o total de E2, embora sejam ocorrências distintas; a agregação perde essa informação individual.

Com dependências fixas `A=[[0,0,0],[0.25,0,0],[0,0.5,0]]`, a segunda transformação é `S(p)=(I-A)⁻¹p`. A composição `C=S∘T=(I-A)⁻¹M` continua linear. Resolver `r=p+Ar` fornece `r1=9`, `r2=11,5+0,25×9=13,75`, `r3=2+0,5×13,75=8,875`. A composição exige `I-A` invertível; no projeto isso é verificado antes de resolver.

## Conferência com o material de apoio do docente

O cenário da aula usa `V2` em **Web e Banco**, e `V4` sem equipamento afetado. Com colunas `V1,V2,V3,V4`:

```text
M = [1 1 0 0]      v = [9,8; 5,3; 7,5; 4,3]
    [0 0 1 0]
    [0 1 0 0]      b = Mv = [15,1; 7,5; 5,3]
```

A segunda coluna tem dois `1`, pois a mesma V2 afeta dois ativos; a quarta é nula. Para `A=[[0,0.2,0],[0.5,0,0],[0,0.6,0]]`, o sistema fica `x1=15,1+0,2x2`, `x2=7,5+0,5x1`, `x3=5,3+0,6x2`. Logo `x≈(18,44;16,72;15,33)`. O script desta pasta confere os valores. O exemplo também mostra uma extensão opcional `F=diag(1,5;1;1)`, que levaria `b` a `(22,65;7,5;5,3)`, mas não é aplicada ao programa principal sem pesos de exposição definidos.
