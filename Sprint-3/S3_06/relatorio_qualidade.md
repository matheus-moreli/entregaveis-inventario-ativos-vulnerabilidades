# S3_06 — qualidade de software e análise estática

Execução em 13/10/2026 sobre a branch de melhoria do Trabalho 2. O arquivo `antes_refatoracao.py` é um exemplo didático de função curta com nomes pouco claros e formatação ruim; `depois_refatoracao.py` usa nomes descritivos, `strip`, docstring e formatação PEP 8. No projeto real, regras antes dispersas em funções de `inventario.py` passaram a métodos de `Inventario`; `persistencia.py` ganhou `RepositorioJSON` e gravação atômica, `risco.py` ganhou `AnalisadorRisco`. As funções antigas ficaram como adaptadores para preservar menu e testes. Essa refatoração reduziu a distância entre modelo de dados e operações, sem alterar o comportamento observado pelos testes.

## Evidência de ferramentas

| Comando | Saída observada |
|---|---|
| `python -m flake8` no projeto principal | nenhuma ocorrência; código de saída 0 |
| `python -m black .` no projeto principal | 9 arquivos formatados, 1 já conforme |
| `python -m black --check .` | 10 arquivos conformes; código de saída 0 |
| `python -m pylint --errors-only app.py modelos.py inventario.py persistencia.py risco.py servico.py` | nenhum erro; código de saída 0 |
| `python -m pylint app.py modelos.py inventario.py persistencia.py risco.py servico.py` | nota 9,29/10; avisos de projeto e estilo analisados abaixo |
| `python -m pylint Sprint-3/S3_06/depois_refatoracao.py` | nota 10,00/10 no exemplo refatorado |

O `pylint` completo aponta, entre outros, muitos argumentos/atributos nos objetos e operações de domínio, alguns docstrings ausentes e duas lambdas locais em laços de `risco.py`. Os argumentos refletem os campos exigidos pelo enunciado, mas podem virar objetos de entrada em evolução futura. O alerta de lambda não causa captura tardia: ela é usada imediatamente por `max` dentro da mesma iteração. As checagens `type(...) is int` são intencionais em campos onde `bool`, subclasse de `int`, deve ser rejeitado. `do_GET` mantém o nome exigido por `BaseHTTPRequestHandler`.

Análise estática detecta estilo e sinais de manutenção, mas não substitui testes. A suíte de 45 testes passou após a formatação; o relatório S3_07 registra cobertura e seus limites.
