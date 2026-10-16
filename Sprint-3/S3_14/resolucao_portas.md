# S3_14 — portas, circuito e Von Neumann

| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

NOT inverte uma entrada. NAND = `¬(A∧B)`, NOR = `¬(A∨B)`, XOR vale 1 quando entradas diferem, XNOR quando são iguais. Um circuito de autorização ilustrativo usa `S=(credencial_válida ∧ permissão) ∧ ¬bloqueado`. Primeiro uma porta AND combina credencial e permissão; uma NOT inverte o bloqueio; a AND final libera apenas quando as três condições são atendidas. Para `(1,1,0)`, S=1; mudar qualquer uma das primeiras para 0 ou bloqueado para 1 produz S=0. A tabela do circuito completo tem oito entradas possíveis e está no script `portas_logicas.py`.

Simplificação: `A∧(A∨B)=A` pela absorção. Conferência: quando A=0, ambos os lados são 0; quando A=1, ambos são 1, independentemente de B. Em hardware, a forma simplificada pode evitar uma OR e uma AND nesse trecho, embora desempenho real dependa da tecnologia e do circuito completo.

Arquitetura de Von Neumann: memória guarda instruções e dados; unidade de controle busca e decodifica instruções; ULA executa operações aritméticas e lógicas; registradores guardam valores imediatos; barramentos transportam endereços, dados e sinais de controle entre CPU, memória e E/S. No ciclo busca–decodificação–execução, o contador de programa identifica a próxima instrução, a CPU a lê pela rede de barramentos, a unidade de controle interpreta a operação e a ULA executa, atualizando registradores/memória. O `if` de autorização em Python é traduzido em instruções que usam comparações e desvios; as portas implementam operações booleanas abaixo da camada de software. Isso é uma relação conceitual, não uma afirmação sobre o circuito específico da máquina usada.
