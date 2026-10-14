# Situação verificável do Trabalho 2 — 13/10/2026

O Trabalho 2 amplia o inventário do Trabalho 1 com classes de domínio, operações de CRUD, persistência JSON, cadastro de vulnerabilidades e análise de riscos. A implementação está na [PR #3 do projeto principal](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/pull/3); estes entregáveis estão na PR correspondente deste repositório.

## Evidências executadas

- 50 testes automatizados do projeto principal passaram localmente, incluindo persistência das dependências, rejeição de matriz singular, cenário de três ativos resolvido à mão, uso de uma instância única de `Inventario` pela interface e atualização do serviço após mudança no JSON. A imagem Docker atual foi reconstruída, executou os 50 testes (2 exclusivos de Windows pulados no Linux), respondeu a `/saude` e `/riscos` com seis ativos e chegou ao estado `healthy`. O job `testes-e-estilo` da [execução 38492072235](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38492072235) passou na PR atualizada.
- A collection de S3_18 executou 9 requisições e 14 asserções com Newman, sem falhas; o resultado está em `Sprint-3/S3_18/resultado_newman.md` e no JSON da mesma pasta.
- O teste de S3_19 comprovou POST, GET, PUT e DELETE da API SQLite. O navegador de S3_17 exibiu um ativo recebido da API; a evidência está na pasta do card.
- Os PDFs alterados foram recompilados com MiKTeX e seu texto pôde ser extraído. Códigos, relatórios e cálculos ficam junto dos respectivos cards.

## Pendências que exigem outra pessoa ou ambiente

- A [issue #4](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/issues/4) descreve a prova de 24 horas com Docker, usando o menu completo em um container com terminal persistente. O container local anterior seguia ativo por cerca de 10 h 17 min sem reinícios, mas usa código antigo. A versão nova (`3395957`) começou a rodar em outro container local em **13/10/2026 21:46:48 BRT**, com menu completo, seis ativos e volume próprio. Ainda faltam 24 horas contínuas dessa versão e sua hospedagem **no servidor do docente**. A comparação item por item com os enunciados está em `docs/conferencia-enunciados.md` da PR principal.
- S1_19, S2_17 e S3_08 pedem participação de outra pessoa em revisão. A PR #3 está em rascunho, sem aprovação/comentário de colega. Conflitos e respostas a comentários só poderão ser demonstrados se ocorrerem de verdade.
- O workflow existente cobre testes Python e flake8. A conta GitHub autenticada não tem escopo `workflow` para publicar uma alteração no próprio workflow; portanto não há job Docker publicado nesta PR.

Esta situação distingue artefato entregue de evidência externa pendente; não transforma checklist do Trello em prova por si só.
