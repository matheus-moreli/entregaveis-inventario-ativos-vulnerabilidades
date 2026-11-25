# Evidências e verificações da Sprint 5

Revisão conferida em 25/11/2026: 1561b80ab4aa7c3404eb0341029f310b0a624646.

| Verificação | Resultado |
|---|---|
| python app.py --testes | 91 testes e 6 subtestes aprovados. |
| python -m black --check app.py apresentacao dominio infraestrutura tests | Formatação aprovada. |
| docker compose config --quiet | Configuração original do projeto validada. |
| python -m pytest laboratorio | 10 testes aprovados para integridade referencial, consultas parametrizadas, redução de consultas e permissões. |
| docker compose -f infra/compose.tls.yaml config --quiet | A configuração do laboratório TLS foi validada. A execução requer Docker e certificados do ambiente. |
| GitHub Actions | CI aprovado na revisão conferida. |
| Tempo ativo da V3 | Registro publicado de 5 dias, 23 horas, 13 minutos e 55 segundos, sem reinícios. A evidência se refere à V3 já implantada na UFU. |
| Contrato OpenAPI | Cópia da revisão conferida com estados de resposta utilizados na coleção Postman. |

- [Código na revisão conferida](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/commit/1561b80ab4aa7c3404eb0341029f310b0a624646)
- [Execução do GitHub Actions](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/actions/runs/45540747428)
- [Evidência histórica do Docker na UFU](https://github.com/matheus-moreli/inventario-ativos-vulnerabilidades/blob/main/docs/evidencias-docker-2026-11-23.md)

## Evidências a coletar no ambiente da disciplina

- Executar a revisão entregue no Docker da UFU. Conferir estado, porta, nome, volume, SHA e saúde após 24 horas. O registro histórico já comprova mais de 24 horas para a V3.
- Registrar a apresentação, a Sprint Review e a demonstração. Preencher a [ata](Review.md) com o feedback real.
- Quando o card pedir execução da ferramenta específica, anexar os resultados de Postman, Schemathesis, Bandit, pip-audit e mypy. As propostas de ORM, JWT e TLS têm configuração e código de laboratório. A implantação externa em nuvem depende do serviço e do ambiente da disciplina.
