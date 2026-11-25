# Arquitetura do inventário

O operador mantém ativos, vulnerabilidades e dependências pelo terminal. A API HTTP permite consulta do inventário e do ranking. O ambiente da UFU executa o serviço em Docker na porta 2217 e guarda os dados em volume persistente.

| Componente | Responsabilidade |
|---|---|
| app.py e apresentacao/ | Entrada do programa, terminal, API e contrato OpenAPI |
| dominio/ | Ativos, vulnerabilidades, validação, dependências e cálculo de risco |
| infraestrutura/ | Leitura e gravação do inventário JSON |
| Docker Compose | Configuração do serviço, verificação de saúde e volume |
| tests/ | Testes de domínio, armazenamento e integração HTTP |

## Decisões de arquitetura

- **ADR 1 — JSON com gravação atômica.** Mantém a instalação simples e reaproveita inventários anteriores. Se houver necessidade de vários processos escrevendo simultaneamente, avaliar migração transacional para banco relacional. O laboratório da S5 permite estudar essa opção.
- **ADR 2 — Escrita pelo terminal e consultas pela API.** Mantém o cadastro e suas validações no fluxo atual. Se forem adicionadas mutações HTTP, exigir autorização por operação, validação e testes de persistência.
- **ADR 3 — Serviço em loopback com volume.** A configuração da UFU reduz a exposição direta e desacopla o inventário do contêiner. Acesso externo autorizado pode ocorrer por túnel. Um proxy TLS pode ser adotado após validação no ambiente de implantação.

## Ameaças e controles

| STRIDE | Situação do inventário | Controle ou verificação proposta |
|---|---|---|
| Falsificação de identidade | Consulta HTTP com credencial indevida | Bearer e testes de resposta 401. Considerar rotação. |
| Adulteração | Alteração ou corrupção do inventário em disco | Validação, gravação atômica, permissões de arquivo e teste de restauração. |
| Repúdio | Impossibilidade de atribuir alterações do terminal | Adotar trilha de auditoria se houver múltiplos operadores. |
| Divulgação | Ativos, relações e riscos expostos | Autenticar consulta, restringir a porta e excluir segredos do histórico. |
| Negação de serviço | Consulta ou falha de persistência prejudica o serviço | Limitar paginação, verificar saúde e tratar falhas de leitura. |
| Elevação de privilégio | Uma mesma credencial cobre operações de consulta | Para futuras escritas HTTP, testar permissões por papel e negar as operações restantes. |

## Backlog verificável

1. Implantar a imagem correspondente à revisão entregue. Registrar SHA, imagem, nome, saúde e tempo ativo após 24h.
2. Testar restauração de um inventário sintético em volume isolado. A listagem, as dependências e o ranking devem coincidir com a origem.
3. Executar os scanners no commit entregue. Anexar versões, saída e tratamento das ocorrências.
4. Se o trabalho exigir migração para ORM, aplicar em cópia de dados. Conferir contagens, vínculos e ranking antes e depois, com rollback documentado.
