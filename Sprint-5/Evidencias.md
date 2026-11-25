# Evidências e verificações da Sprint 5

Revisão conferida em 25/11/2026: bb40a3842268f797e6520eb3bf1e1c6bdb4aae14.

| Verificação | Resultado |
|---|---|
| python app.py --testes | 101 testes e 6 subtestes aprovados, incluindo a conferência independente com NumPy. |
| python -m black --check . e python -m flake8 | Formatação e estilo aprovados. |
| docker compose config --quiet | Configuração original do projeto validada. |
| python -m pytest laboratorio | 10 testes aprovados para integridade referencial, consultas parametrizadas, redução de consultas e permissões. |
| docker compose -f infra/compose.tls.yaml config --quiet | A configuração do laboratório TLS foi validada. A execução requer Docker e certificados do ambiente. |
| GitHub Actions | CI aprovado na revisão conferida. |
| Tempo ativo da V3 | Registro publicado de 5 dias, 23 horas, 13 minutos e 55 segundos, sem reinícios. A evidência se refere à V3 já implantada na UFU. |
| Contrato OpenAPI | Cópia da revisão conferida com estados de resposta utilizados na coleção Postman. |

- [Código na revisão conferida](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/commit/bb40a3842268f797e6520eb3bf1e1c6bdb4aae14)
- [Execução do GitHub Actions](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/45541722526)
- [Evidência histórica do Docker na UFU](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/blob/main/docs/evidencias-docker-2026-11-23.md)

## Evidências a coletar no ambiente da disciplina

- Executar a revisão entregue no Docker da UFU. Conferir estado, porta, nome, volume, SHA e saúde após 24 horas. O registro histórico já comprova mais de 24 horas para a V3.
- Registrar a apresentação, a Sprint Review e a demonstração. Preencher a [ata](Review.md) com o feedback real.
- Quando o card pedir execução da ferramenta específica, anexar os resultados de Postman, Schemathesis, Bandit, pip-audit e mypy. As propostas de ORM, JWT e TLS têm configuração e código de laboratório. A implantação externa em nuvem depende do serviço e do ambiente da disciplina.
