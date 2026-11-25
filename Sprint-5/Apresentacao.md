# Apresentação do Trabalho 02

Abra os [slides](Slides-UFU.html). A demonstração pode usar um inventário sintético com um notebook e um servidor.

| Tempo | O que mostrar |
|---|---|
| 0:00–0:40 | Apresentar o problema de identificar ativos e priorizar vulnerabilidades. |
| 0:40–1:35 | Cadastrar dois ativos, inserir vulnerabilidades e vincular a dependência no terminal. |
| 1:35–2:40 | Mostrar o cálculo do risco próprio e o efeito da dependência, com as matrizes. |
| 2:40–3:25 | Mostrar persistência após reiniciar e consultar saúde e riscos na API. |
| 3:25–4:20 | Mostrar o resultado do pytest, o CI e a evidência histórica de Docker. |
| 4:20–5:00 | Explicar a escolha de JSON e as extensões estudadas na S5. |

## Perguntas para a apresentação

1. **O que evoluiu desde o Trabalho 01?** O inventário ganhou separação de responsabilidades, estrutura de ativos, dependências, ranking, persistência aprimorada e operação em Docker.
2. **Por que POO?** Cadastro e validação ficam próximos dos modelos de ativo, com especialização onde as categorias têm dados diferentes.
3. **Como o dado sobrevive ao reinício?** O JSON fica no volume montado em /app/dados e o repositório o lê na inicialização.
4. **Onde entra álgebra linear?** A matriz de vulnerabilidades, o vetor de pontuações e a matriz de exposição calculam o risco próprio. A matriz de dependências permite representar a transmissão de risco entre ativos.
5. **Qual é um exemplo numérico?** No modelo ilustrativo, o fator de exposição 0,6 faz o CVSS 5 contribuir com 3 no notebook. Um servidor com risco próprio 4 que herda metade desse valor chega a 5,5. Explique a matriz de dependências e mostre os fatores realmente usados na demonstração.
6. **Por que JSON e ORM em separado?** JSON mantém a operação atual com poucas dependências. O laboratório avalia consultas e relacionamentos que podem justificar banco relacional futuramente.
7. **Como o aplicativo trata consultas inválidas?** O contrato mostra erros de autenticação e validação. A suíte testa o comportamento das rotas.
8. **Como verificar o Docker?** Conferir nome e estado, consultar /saude e medir o tempo desde o início. A prova histórica deve ser identificada como referente à V3.
9. **Qual o papel do pytest?** Exercitar cálculo, persistência e integração para detectar regressões em mudanças futuras.
10. **Qual é o ponto principal da S5?** Demonstrar API documentada, testes, empacotamento e revisão de segurança, distinguindo o serviço atual dos exercícios de ORM, autenticação e TLS.
