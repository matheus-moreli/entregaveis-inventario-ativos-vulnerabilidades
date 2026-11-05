# Sprint 4 - Entregáveis

Esta pasta contém os vinte cards `S4_01` a `S4_20`. Cada card possui:

- `entregavel.tex`: fonte LaTeX;
- `entregavel.pdf`: documento pronto para anexar e ler;
- um arquivo complementar com exemplo, roteiro ou evidência do assunto.

## Organização

Os cards S4_01 a S4_05 ligam arquitetura, POO, JSON e cliente-servidor ao
Inventário de Ativos. S4_06 e S4_07 trazem SQL didático. S4_08 a S4_13 contêm
estruturas de dados, algoritmos e complexidade. S4_14 registra a suíte de testes
automáticos com Pytest. S4_15 a S4_20 documentam Docker, monitoramento, Linux e
integração.

## Estado honesto dos cards de infraestrutura

Por orientação do aluno, Docker, compose e servidor **não foram executados nesta
etapa**. Os documentos desses cards trazem arquivos de preparação, critérios de
aceite e o roteiro de conferência; não alegam container criado, deploy feito ou
execução de 24 horas.

## Como conferir o projeto principal

Na pasta do projeto principal, execute:

```powershell
python -m unittest -v
python -m pytest -q
python -m flake8 .
```

O primeiro e o segundo comando executam os testes automatizados. O último confere
o estilo. Para utilizar o sistema, execute `python app.py` no Windows.

## Regenerar os PDFs

Os PDFs foram gerados com o `gerar_entregaveis.py`. Com MiKTeX instalado, execute:

```powershell
python gerar_entregaveis.py
```

O script atualiza os PDFs a partir do conteúdo definido nele e mantém apenas os
arquivos finais, sem logs auxiliares.
