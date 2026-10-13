# S3_13 — lógica proposicional aplicada

Considere:

- P: “o ativo está cadastrado”;
- Q: “a vulnerabilidade possui CVSS válido”.

A regra de cadastro seguro é P AND Q. Ela só é verdadeira quando os dois requisitos
são verdadeiros. Em Python, a mesma ideia é uma condição que exige ativo e
CVSS válido.

Negar P AND Q equivale a NOT P OR NOT Q. Isso é útil para bloquear uma operação
quando falta o ativo ou quando a nota CVSS é inválida.
