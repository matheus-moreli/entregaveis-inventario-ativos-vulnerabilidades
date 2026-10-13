# S3_18 — coleção Postman

O arquivo `postman_collection.json` contém quatro requisições encadeadas:

1. GET /ativos, para listar os registros;
2. POST /ativos, para cadastrar um ativo de exemplo.
3. PUT /ativos/{id}, para atualizar o ativo criado;
4. DELETE /ativos/{id}, para remover o ativo criado.

Depois do POST, a collection armazena o identificador retornado na variável
`ativoId`. O PUT e o DELETE reutilizam essa variável, validando um fluxo CRUD
completo, não apenas chamadas isoladas.

Para executar no Postman:

1. iniciar a API com python api.py dentro da pasta S3_19;
2. abrir o Postman e escolher Import;
3. selecionar postman_collection.json;
4. executar a collection e conferir os códigos 200, 201, 200 e 204.

A collection foi executada em 13/10/2026 pelo Newman 11.16.0, executor de
collections do Postman. Foram quatro requisições e quatro assertions aprovadas,
sem falhas. O resultado está registrado em `resultado_newman.md`.
