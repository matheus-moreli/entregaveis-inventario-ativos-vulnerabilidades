# SOLID aplicado sem exagero

- **Responsabilidade única:** cada arquivo tem uma função principal.
- **Aberto/fechado:** novos tipos de ativo podem herdar de Equipamento sem reescrever o CRUD.
- **Substituição:** Notebook e Servidor podem ser tratados como Equipamento.
- **Interface pequena:** o terminal pede apenas operações necessárias ao Inventario.
- **Dependência:** regras não dependem de input/print, portanto podem ser testadas.

O objetivo é organização, não criar classes vazias.
