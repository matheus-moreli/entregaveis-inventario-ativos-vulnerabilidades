# S3_18 — execução real da collection

Em 13/10/2026, a collection `postman_collection.json` foi executada com Newman 6.2.3 contra a API Flask local de S3_19 em `127.0.0.1:5000`. Comando: `npx --yes newman run Sprint-3/S3_18/postman_collection.json`. Uma segunda execução usou `--reporters json --reporter-json-export Sprint-3/S3_18/resultado_newman.json`; o arquivo JSON é a evidência bruta exportada pela ferramenta.

**Resultado:** 9 requisições, 14 assertions, 0 falhas. A sequência criou um ativo com nome único, guardou o ID em `ativoId`, atualizou, confirmou o nome via GET, removeu e confirmou ausência via GET. Também testou POST sem nome (400), PUT de ID inexistente (404) e DELETE de ID inexistente (404). Os asserts conferem status e conteúdo JSON quando aplicável, não só o código HTTP.

| Operação | Status obtido | Verificação adicional |
|---|---:|---|
| GET lista inicial | 200 | corpo é lista JSON |
| POST válido | 201 | ID numérico e nome devolvidos |
| PUT válido | 200 | mensagem de atualização |
| GET após PUT | 200 | nome alterado presente |
| DELETE válido | 204 | corpo vazio |
| GET após DELETE | 200 | ID ausente |
| POST inválido | 400 | erro em JSON |
| PUT inexistente | 404 | erro de não encontrado |
| DELETE inexistente | 404 | erro de não encontrado |

A execução ocorreu em servidor de desenvolvimento local. Ela prova o fluxo dessa API didática, não o modo Docker do projeto principal nem permanência por 24 horas.
