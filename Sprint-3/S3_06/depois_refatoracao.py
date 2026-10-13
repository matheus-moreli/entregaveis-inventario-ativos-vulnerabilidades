"""Exemplo do mesmo cadastro após a refatoração guiada pelo PEP 8."""


def cadastrar_ativo(nome, tipo, responsavel):
    """Valida os campos obrigatórios e monta o registro de um ativo."""
    if not nome.strip() or not tipo.strip():
        return None

    return {
        "nome": nome.strip(),
        "tipo": tipo.strip(),
        "responsavel": responsavel.strip(),
    }
