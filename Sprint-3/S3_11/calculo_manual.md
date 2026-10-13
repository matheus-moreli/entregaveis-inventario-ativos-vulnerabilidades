# S3_11 — inversa, determinante e risco

Para `B=[[2,1],[1,1]]`, `det(B)=2×1−1×1=1`. Pela fórmula 2×2, `B⁻¹=(1/det)[[d,-b],[-c,a]]=[[1,-1],[-1,2]]`. A multiplicação `BB⁻¹=I` confirma. Geometricamente, `det=1` preserva área orientada e a transformação não colapsa o plano.

Para `C=[[1,2,0],[0,1,1],[1,0,1]]`, Sarrus: diagonais positivas `1×1×1+2×1×1+0=3`; diagonais negativas somam zero, então `det(C)=3`. Pela expansão de cofatores da primeira linha: `1×det[[1,1],[0,1]]−2×det[[0,1],[1,1]]=1−2(−1)=3`. O mesmo valor por métodos independentes evita erro de sinal. Como `det≠0`, a imagem ocupa R³ e existe inversa.

Para mostrar singularidade **com cada peso estritamente menor que 1**, use três ativos com peso `0.5` para cada um dos outros dois: `A=[[0,0.5,0.5],[0.5,0,0.5],[0.5,0.5,0]]`. Cada entrada não nula satisfaz `0≤Aij<1`, mas cada linha soma 1. Portanto `(I-A)(1,1,1)=(0,0,0)`; `I-A` tem núcleo não trivial e determinante zero. Não existe inversa nem solução única para todo `b`.

O programa principal exige soma de pesos por ativo **menor** que 1. Nesse domínio, `I-A` é estritamente diagonal dominante por linhas: diagonal 1 e soma dos módulos fora da diagonal menor que 1. Uma matriz estritamente diagonal dominante é não singular. A checagem numérica de invertibilidade permanece como defesa adicional. Geometricamente, o caso singular comprime a direção `(1,1,1)` em zero e perde informação.
