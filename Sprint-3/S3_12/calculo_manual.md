# S3_12 — erros numéricos no risco

IEEE 754 binary64 armazena uma aproximação finita para muitos decimais: em Python, `repr(0.1+0.2)` resulta em `0.30000000000000004`. Erro absoluto é `|aproximado−referência|`; erro relativo é esse erro dividido por `|referência|` quando a referência é não zero. Para essa soma, erro absoluto ≈ `5,55×10⁻¹⁷` e relativo ≈ `1,85×10⁻¹⁶`. Comparar floats por igualdade exata nesse caso é inadequado; usar tolerância coerente com a escala.

**Truncamento e arredondamento:** para 6,8085106, truncar a duas casas dá 6,80; arredondar à casa mais próxima dá 6,81. O erro absoluto é, respectivamente, ≈0,0085106 e ≈0,0014894. Arredondamento costuma reduzir o erro local, mas nenhuma das operações corrige um modelo mal condicionado.

No exemplo de risco, `B=I-A=[[1,-0.2],[-0.3,1]]`, `p=(8,4)`. O determinante é 0,94 e a solução exata em frações é `r=(440/47,320/47)≈(9,36170213,6,80851064)`. O residual `e=Br−p` para a solução de `numpy.linalg.solve` deve ficar perto do erro de máquina; o script imprime a norma infinita `max(|e_i|)`. Comparar com `numpy.linalg.inv(B)@p` ilustra que resolver diretamente evita formar uma inversa numérica desnecessária.

O número de condição `κ(B)=||B||·||B⁻¹||` mede amplificação potencial de perturbações: matriz quase singular pode transformar pequena alteração dos dados em grande alteração de `r`. O script também mostra uma matriz 2×2 mal condicionada. Um residual pequeno indica que o resultado satisfaz bem as equações computadas, mas não garante pequena diferença da solução verdadeira quando `κ` é grande. Verificar condicionamento, residual e domínio dos pesos antes de apresentar riscos.
