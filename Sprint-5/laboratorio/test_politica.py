import pytest

from politica import permite


@pytest.mark.parametrize(
    ("papel", "acao", "esperado"),
    [
        ("leitor", "consultar", True),
        ("leitor", "atualizar", False),
        ("operador", "cadastrar", True),
        ("operador", "excluir", False),
        ("administrador", "backup", True),
        ("desconhecido", "consultar", False),
        ("administrador", "acao_desconhecida", False),
    ],
)
def test_permissao(papel, acao, esperado):
    assert permite(papel, acao) is esperado
