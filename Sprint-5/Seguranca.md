# Revisão de segurança

Revisão estática na versão 1561b80. Depois dela, o commit 797ec94 removeu as rotas-isca e o bb40a38 acrescentou testes de conferência com NumPy; nenhum dos dois altera as conclusões abaixo. A coluna de verificação futura orienta o encerramento das lacunas identificadas.

| OWASP Top 10 2025 | Controle observado ou cenário | Verificação futura |
|---|---|---|
| A01 | Consultas de ativos e riscos protegidas por Bearer | Formalizar autorização por papel antes de disponibilizar escrita HTTP. |
| A02 | Compose vinculado ao loopback por padrão | Conferir as variáveis efetivas e as portas no host da UFU. |
| A03 | Dependências declaradas e instalação em CI | Executar pip-audit na versão entregue e registrar a resolução das ocorrências. |
| A04 | Autenticação por token na API | Para tráfego que sai do host, validar TLS no acesso autorizado. |
| A05 | Persistência da aplicação em JSON. No laboratório SQLite, as consultas usam parâmetros. | Se houver ORM, manter parâmetros para valores e uma lista de campos de ordenação permitidos. |
| A06 | Separação entre terminal e acesso HTTP de leitura | Revisar arquitetura antes de adicionar escrita HTTP ou perfis. |
| A07 | Credencial necessária para consultar dados protegidos | Adotar rotação e verificar respostas para credenciais ausentes e inválidas. |
| A08 | GitHub CI testa a revisão publicada | Vincular a imagem à revisão e registrar seu digest na implantação. |
| A09 | Endpoint de saúde e histórico operacional documentado | Registrar eventos de implantação e monitorar falhas em produção. |
| A10 | Contrato documenta respostas de erro | Verificar indisponibilidade de armazenamento e preservar a resposta pública sem segredos. |

[OWASP Top 10 2025](https://top10.owasp.org/2025/pt-BR/)

## Autorização proposta para extensão web

| Operação | Leitor | Operador | Administrador |
|---|---|---|---|
| Consultar ativos e riscos | Sim | Sim | Sim |
| Cadastrar e atualizar | Não | Sim | Sim |
| Excluir, gerenciar acessos e exportar backup | Não | Não | Sim |

O Bearer atual serve as consultas já implementadas. No laboratório, ação ou papel desconhecidos são negados. Para uma futura sessão web, configurar cookies Secure, HttpOnly e SameSite conforme os fluxos esperados, renovar a sessão após autenticação, expirar sessões no servidor e validar proteção CSRF para operações de escrita. Guardar apenas o hash Argon2id das senhas. Para JWT, controlar a validade, o emissor, a audiência e o algoritmo de verificação. Preservar o segredo fora do Git.

## Verificações de implantação

- Conferir usuário do contêiner, limites, porta local e montagem do volume. Executar teste de restauração usando cópia.
- Validar a configuração do proxy e certificados antes de habilitar TLS. Usar o nome e a porta que constam da evidência do trabalho.
- Rodar Bandit e pip-audit no ambiente da disciplina. Registrar data, versão, saída e tratamento dos achados.
