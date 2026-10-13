"""Teste simples dos quatro verbos CRUD da API do entregável S3_19."""

import gc
from pathlib import Path

import api


def executar():
    """Cria uma base temporária e confirma cadastro, consulta, edição e remoção."""
    banco_original = api.CAMINHO_BANCO
    banco_teste = Path(__file__).with_name("inventario_teste.db")
    if banco_teste.exists():
        banco_teste.unlink()

    api.CAMINHO_BANCO = banco_teste
    api.iniciar_banco()
    cliente = api.app.test_client()

    cadastro = cliente.post(
        "/ativos",
        json={"nome": "Servidor de teste", "tipo": "Servidor", "responsavel": "TI"},
    )
    assert cadastro.status_code == 201
    identificador = cadastro.get_json()["id"]

    consulta = cliente.get("/ativos")
    assert consulta.status_code == 200
    assert len(consulta.get_json()) == 1

    edicao = cliente.put(
        f"/ativos/{identificador}",
        json={"nome": "Servidor atualizado", "tipo": "Servidor", "responsavel": "TI"},
    )
    assert edicao.status_code == 200

    remocao = cliente.delete(f"/ativos/{identificador}")
    assert remocao.status_code == 204
    assert cliente.get("/ativos").get_json() == []

    api.CAMINHO_BANCO = banco_original
    del cliente
    gc.collect()
    banco_teste.unlink()
    print("CRUD comprovado: POST, GET, PUT e DELETE responderam como esperado.")


if __name__ == "__main__":
    executar()
