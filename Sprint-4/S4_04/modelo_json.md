# Modelo JSON

```json
{
  "id": 2,
  "nome": "SRV-WEB-01",
  "tipo": 2,
  "vulnerabilidades": [{"cve": "CVE-2026-0001", "cvss": 8.0}],
  "dependencias": [{"ativo_id": 1, "peso": 0.25}]
}
```

O repositório grava uma lista desses objetos. Ao carregar, valida ID, dados obrigatórios, CVSS e dependências antes de aceitar a base.
