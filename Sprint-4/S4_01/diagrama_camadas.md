# Diagrama de camadas

```text
Usuário
  |
interface.py (menus, teclas e mensagens)
  |
inventario.py (regras e operações)
  |-----------------------------|
modelos.py (Ativo e Vulnerabilidade)  risco.py (matrizes e Gauss)
  |
persistencia.py (JSON)
  |
dados/inventario.json
```

A interface não valida regra de negócio por conta própria. A persistência não imprime menus. Essa separação permite testar cada parte isoladamente.
