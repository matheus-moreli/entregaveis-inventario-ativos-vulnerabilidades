# Execução da collection Postman

Data da execução: 13/10/2026.

A collection `postman_collection.json` foi executada pelo Newman, o executor de collections do Postman, contra a API Flask local da S3_19.

Comando utilizado:

```text
newman run postman_collection.json
```

Versão do Newman: 11.16.0.

Resultado: **4 requisições executadas, 4 assertions aprovadas, 0 falhas.**

| Requisição | Resultado esperado | Resultado obtido |
|---|---:|---:|
| `GET /ativos` | 200 | 200 OK |
| `POST /ativos` | 201 | 201 Created |
| `PUT /ativos/{id}` | 200 | 200 OK |
| `DELETE /ativos/{id}` | 204 | 204 No Content |

O `POST` armazenou o identificador do ativo criado na variável `ativoId`; esse mesmo identificador foi usado no `PUT` e no `DELETE`. Portanto, a execução comprovou o fluxo CRUD completo e não apenas chamadas isoladas.
