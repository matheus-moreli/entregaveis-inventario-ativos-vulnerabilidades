# Situação verificável do Trabalho 2 — 13/10/2026

O Trabalho 2 amplia o inventário do Trabalho 1 com classes de domínio, operações de CRUD, persistência JSON, cadastro de vulnerabilidades e análise de riscos. A implementação está na [PR #3 do projeto principal](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/pull/3); estes entregáveis estão na PR correspondente deste repositório.

## Evidências executadas

- 47 testes automatizados do projeto principal passaram localmente, incluindo persistência das dependências e rejeição de matriz singular. O job `testes-e-estilo` da [execução 38478653977](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38478653977) também passou após essas alterações.
- A collection de S3_18 executou 9 requisições e 14 asserções com Newman, sem falhas; o resultado está em `Sprint-3/S3_18/resultado_newman.md` e no JSON da mesma pasta.
- O teste de S3_19 comprovou POST, GET, PUT e DELETE da API SQLite. O navegador de S3_17 exibiu um ativo recebido da API; a evidência está na pasta do card.
- Os PDFs alterados foram recompilados com MiKTeX e seu texto pôde ser extraído. Códigos, relatórios e cálculos ficam junto dos respectivos cards.

## Pendências que exigem outra pessoa ou ambiente

- A [issue #4](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/issues/4) descreve a prova de 24 horas com Docker, agora usando o menu completo em um container com terminal persistente. Docker não está disponível nesta máquina; imagem e operação contínua ainda não foram verificadas. A comparação item por item com os dois enunciados oficiais está em `docs/conferencia-enunciados.md` da PR do projeto principal.
- S1_19, S2_17 e S3_08 pedem participação de outra pessoa em revisão. A PR #3 está em rascunho, sem aprovação/comentário de colega. Conflitos e respostas a comentários só poderão ser demonstrados se ocorrerem de verdade.
- O workflow existente cobre testes Python e flake8. A conta GitHub autenticada não tem escopo `workflow` para publicar uma alteração no próprio workflow; portanto não há job Docker publicado nesta PR.

Esta situação distingue artefato entregue de evidência externa pendente; não transforma checklist do Trello em prova por si só.
