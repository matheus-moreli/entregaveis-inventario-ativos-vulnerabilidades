# Evidência de integração contínua

O workflow `Verificar projeto` foi publicado no repositório principal em 13/10/2026. A melhoria do Trabalho 2 está na [Pull Request #3](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/pull/3), aberta da branch `melhoria-trabalho-2-completo` para `main`.

- Arquivo: [`.github/workflows/verificar.yml`](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/blob/main/.github/workflows/verificar.yml)
- Execução: [run #1 concluído com sucesso](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38445859084)
- Commit que acionou a execução: [`94f1a73`](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/commit/94f1a73ed6eecc528e2f752ef2cf6443a4c81cc5)

O job instala o `flake8`, executa os testes automatizados com `python -m unittest -v` e confere o estilo com `python -m flake8`. A execução verde demonstra que os testes e a verificação de estilo foram automatizados no GitHub Actions.

Na PR #3, o job [testes-e-estilo passou](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38472278580/job/115554131520). A revisão por outra pessoa e a resolução de conflitos não ocorreram nesta PR; permanecem pendências reais, sem simulação. O workflow publicado verifica Python e estilo; a prova Docker está separada na [issue #4](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/issues/4).
