# S3_17 — execução da integração assíncrona

Em 13/10/2026, executei a API Flask de S3_19 em `127.0.0.1:5000` e servi o `index.html` de S3_17 em `127.0.0.1:8000`. Cadastrei na base de demonstração um ativo fictício: **Servidor de demonstração**, tipo **Servidor**.

No navegador, cliquei em **Carregar ativos**. A página exibiu `1 ativo(s) carregado(s).` e o item `Servidor de demonstração - Servidor`. Isso comprova o fluxo Fetch API → resposta JSON → atualização da interface. O código também trata erro HTTP, formato inesperado e falha de comunicação; os dados são inseridos com `textContent`, sem interpretar HTML recebido da API.

Dados de teste são locais e fictícios. A execução não depende de login.
