# Status verificável - Inventário de Ativos e Vulnerabilidades

Este arquivo mostra o estado atual sem transformar documentação em prova de execução.
Atualizado em 25/11/2026.

## Pronto e publicado

- Projeto principal (commit `bb40a38`): CRUD de ativos e vulnerabilidades, persistência
  JSON em lista de objetos, orientação a objetos com fator de exposição por tipo,
  cálculo de risco próprio e efetivo por álgebra linear, dependências, simulação sem
  salvar e serviço HTTP de consulta protegido por senha.
- Testes: 101 testes aprovados (`python app.py --testes`), incluindo a conferência
  independente do modelo de risco com NumPy. Formatação (Black) e estilo (flake8)
  conferidos, e o CI do GitHub passa em Linux, Windows e Docker.
- Docker: o registro de 23/11/2026 comprova mais de 24 horas sem reinícios nas versões
  V1 (6 dias, 22 h) e V3 (5 dias, 23 h 13 min), no servidor da disciplina. Os dados vêm de
  `docker inspect` e de `/saude`, coletados no servidor.
- Entregáveis: as pastas `Sprint-1` a `Sprint-5` concentram os documentos de cada card.

## Ainda não executado

- A versão final, com `compose.yaml`, ainda será implantada no servidor da disciplina.
  Enquanto isso não ocorrer e passar 24 horas, não há evidência de execução dessa versão.
- Os itens marcados como pendentes em [Sprint-5/README.md](Sprint-5/README.md), como
  mypy, pip-audit, Bandit, Schemathesis, publicação em nuvem e ensaio da apresentação.

## Dependências externas

Revisão de colega, comentários em pull request e demonstração de conflito só
podem ser comprovados quando outra pessoa participar de verdade. Não foram
inventados como evidência.

## Links

- Projeto principal: <https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades>
- Entregáveis: <https://github.com/matheus-moreli/entregaveis-inventario-ativos-vulnerabilidades>
