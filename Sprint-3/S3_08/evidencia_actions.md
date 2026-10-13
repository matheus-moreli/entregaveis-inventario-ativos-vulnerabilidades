# Evidência de integração contínua

O workflow `Verificar projeto` foi publicado no repositório principal em 13/10/2026.

- Arquivo: [`.github/workflows/verificar.yml`](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/blob/main/.github/workflows/verificar.yml)
- Execução: [run #1 concluído com sucesso](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/38445859084)
- Commit que acionou a execução: [`94f1a73`](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/commit/94f1a73ed6eecc528e2f752ef2cf6443a4c81cc5)

O job instala o `flake8`, executa os testes automatizados com `python -m unittest -v` e confere o estilo com `python -m flake8`. A execução verde demonstra que os testes e a verificação de estilo foram automatizados no GitHub Actions.
