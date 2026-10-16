# S3_07 — testes e cobertura do Trabalho 2

Em 13/10/2026, `python -m unittest -q` executou **47 testes** com resultado `OK`. Eles cobrem cadastro, duplicidade, validações de fronteira, consulta, atualização sem alteração parcial, exclusão cancelada e confirmada com limpeza de vínculos, serialização JSON, proteção contra falha de gravação, subclasses, dependências persistidas, rejeição de matriz singular, risco próprio/efetivo e respostas do modo de serviço. A API demonstrativa de S3_19 possui teste próprio e passou separadamente.

Para reproduzir a cobertura: na raiz do projeto principal, `python -m coverage run -m unittest` e `python -m coverage report`. O arquivo `.coveragerc` limita a análise ao código da aplicação, sem inflar o percentual com as linhas dos testes.

| Módulo | Linhas executáveis | Cobertura |
|---|---:|---:|
| interface.py | 666 | 29% |
| inventario.py | 331 | 84% |
| modelos.py | 80 | 92% |
| persistencia.py | 62 | 89% |
| risco.py | 77 | 100% |
| servico.py | 36 | 56% |
| **Total** | **1252** | **56%** |

O total é limitado pela interface interativa, que tem muitos caminhos de teclado difíceis de exercitar em teste unitário, e pelo servidor HTTP, cujo método de escuta ainda não foi coberto por teste local. O CI atual executa testes e estilo, mas ainda não constrói o container. Cobertura mede linhas percorridas, não correção completa. O caso de integridade `test_falha_na_substituicao_preserva_json_anterior` foi acrescentado após a mudança para gravação atômica; simula falha em `os.replace` e confirma que o JSON anterior fica intacto e o arquivo temporário é removido. Outro teste confirma a exclusão do ativo com suas vulnerabilidades e dependências.

**Limite da evidência:** não há log preservado de um teste vermelho anterior à correção nesta entrega. A descrição acima relata os casos e saídas que foram efetivamente executados; não apresenta uma falha inventada.
