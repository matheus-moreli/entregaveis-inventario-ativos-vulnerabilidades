# S3_17 — verificação da integração assíncrona

O frontend foi servido localmente e consumiu a rota GET /ativos da API Flask do
S3_19. A API respondeu HTTP 200, com cabeçalho CORS liberando a origem local.

Ao clicar em Carregar ativos, a página mostrou: 0 ativo(s) carregado(s). Esse
resultado é correto para a base de demonstração vazia. O importante é que a
requisição fetch foi concluída, tratada com async/await e exibida na página.
