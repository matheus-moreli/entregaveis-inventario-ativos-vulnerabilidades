# Cliente, serviço e domínio

```text
Terminal -> InterfaceTerminal -> Inventario -> Modelos/JSON
                                  |
                                  -> risco.py
Serviço HTTP somente leitura ------^
```

O terminal e o serviço podem consultar a mesma regra. A regra não precisa saber se o pedido veio de uma tela ou de uma rota HTTP.
