# S3_06 — qualidade de software

## Antes e depois

antes_refatoracao.py é propositalmente um exemplo curto com nomes pouco claros,
sem espaços adequados e sem documentação. Ele representa um código que até funciona,
mas dificulta manutenção.

Em depois_refatoracao.py, foram aplicados:

- nomes que explicam os dados recebidos;
- validação com strip(), evitando aceitar apenas espaços;
- docstring explicando a responsabilidade da função;
- formatação compatível com PEP 8.

## Conferência reproduzível

Na pasta raiz do Trabalho 2, foram executados flake8 e unittest.
Resultado: nenhuma ocorrência do flake8 e 40 testes aprovados. Para este recorte,
também é possível executar black --check depois_refatoracao.py e
flake8 depois_refatoracao.py.

As ferramentas não substituem a leitura do código: elas ajudam a manter um padrão,
enquanto a função continua curta e adequada ao nível do trabalho.
