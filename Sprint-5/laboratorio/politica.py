PERMISSOES = {
    "leitor": {"consultar"},
    "operador": {"consultar", "cadastrar", "atualizar"},
    "administrador": {
        "consultar", "cadastrar", "atualizar", "excluir", "gerenciar_acessos", "backup"
    },
}


def permite(papel: str, acao: str) -> bool:
    return acao in PERMISSOES.get(papel, set())
