# Situação verificável do Trabalho 2 — 13/10/2026

O Trabalho 2 amplia o inventário do Trabalho 1 com classes de domínio, operações de CRUD, persistência JSON, cadastro de vulnerabilidades e análise de riscos. A implementação está na [PR #3 do projeto principal](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/pull/3); estes entregáveis estão na PR correspondente deste repositório.

## Evidências executadas

- 53 testes automatizados do projeto principal passaram localmente, incluindo o exemplo da aula com a mesma CVE em dois ativos, cálculo do número de condição, persistência das dependências, rejeição de matriz singular, uso de uma instância única de `Inventario` pela interface e atualização do serviço após mudança no JSON. A imagem Docker candidata executou 53 testes (2 exclusivos de Windows pulados no Linux), respondeu a `/saude` e `/riscos` com seis ativos e chegou ao estado `healthy`. O job `testes-e-estilo` da [execução 38493875814](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38493875814) passou na PR atualizada.
- A collection de S3_18 executou 9 requisições e 14 asserções com Newman, sem falhas; o resultado está em `Sprint-3/S3_18/resultado_newman.md` e no JSON da mesma pasta.
- O teste de S3_19 comprovou POST, GET, PUT e DELETE da API SQLite. O navegador de S3_17 exibiu um ativo recebido da API; a evidência está na pasta do card.
- Os PDFs alterados foram recompilados com MiKTeX e seu texto pôde ser extraído. Códigos, relatórios e cálculos ficam junto dos respectivos cards.
- O material **Aula CIBER Risco** foi conferido com S3_09 e S3_12: matriz de incidência com CVE compartilhada e coluna nula ilustrativa, resultado manual `x ≈ (18,44; 16,72; 15,33)` e análise de condicionamento. O app usa κ∞; o slide mostra κ₂.

## Pendências que exigem outra pessoa ou ambiente

- A [issue #4](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/issues/4) descreve a prova de 24 horas com Docker, usando o menu completo em um container com terminal persistente. Nas inspeções de **19/10 e 20/10**, o Docker Desktop estava indisponível e o mesmo container da versão final `4e9d6ad` mostrou um novo `StartedAt` a cada abertura. O início mais recente é **20/10/2026 22:19:12 BRT**. Nenhuma execução anterior tem 24 horas contínuas comprovadas. O menu e os seis ativos persistidos continuam presentes. Ainda faltam 24 horas verificadas da execução atual e hospedagem **no servidor do docente**. O histórico detalhado está em `docs/evidencia-docker-24h.md` da PR principal.
- S1_19, S2_17 e S3_08 pedem participação de outra pessoa em revisão. A PR #3 está em rascunho, sem aprovação/comentário de colega. Conflitos e respostas a comentários só poderão ser demonstrados se ocorrerem de verdade.
- O workflow existente cobre testes Python e flake8. A conta GitHub autenticada não tem escopo `workflow` para publicar uma alteração no próprio workflow; portanto não há job Docker publicado nesta PR.

Esta situação distingue artefato entregue de evidência externa pendente; não transforma checklist do Trello em prova por si só.
