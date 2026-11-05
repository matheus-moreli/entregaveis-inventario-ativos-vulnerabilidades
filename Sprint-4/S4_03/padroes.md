# Padrões identificados

`criar_ativo` atua como uma fábrica simples: recebe o tipo e devolve a classe correta. `Inventario` é uma fachada para o CRUD: a interface pede cadastrar, buscar ou atualizar sem conhecer todos os detalhes internos.

Esses padrões aparecem no código porque reduzem condicionais e duplicação; não foram adicionados frameworks ou estruturas extras.
