# Modelo entidade-relacionamento

ATIVO (1) possui (N) VULNERABILIDADE.

ATIVO: id, nome, tipo, responsavel.
VULNERABILIDADE: id, ativo_id, descricao, cvss.

Um ativo pode possuir nenhuma ou várias vulnerabilidades. Cada vulnerabilidade
pertence a um único ativo.
