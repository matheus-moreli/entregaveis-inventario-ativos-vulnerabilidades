# S3_18 — uso da collection Postman

1. Na pasta `Sprint-3/S3_19`, execute `python api.py`; a API de demonstração inicia em `http://127.0.0.1:5000`. Use somente ambiente local de teste, pois esse servidor Flask está em modo de desenvolvimento.
2. Na raiz do repositório de entregáveis, execute `npx --yes newman run Sprint-3/S3_18/postman_collection.json` ou importe o JSON no Postman e execute a collection inteira, na ordem.
3. Confirme 9 requisições, 14 assertions e 0 falhas. A collection cria um nome único a cada execução e guarda o ID retornado em `ativoId`; por isso pode ser repetida sem conflito.

O fluxo verifica GET da lista, POST, PUT, GET de confirmação, DELETE, GET de confirmação e três casos de erro (POST 400, PUT 404, DELETE 404). O arquivo `resultado_newman.md` explica cada assert e `resultado_newman.json` contém a exportação bruta da execução real em 13/10/2026.
