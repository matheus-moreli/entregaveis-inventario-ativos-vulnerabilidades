import sqlite3
from pathlib import Path

import pytest


@pytest.fixture
def banco():
    conexao = sqlite3.connect(":memory:")
    conexao.execute("PRAGMA foreign_keys = ON")
    conexao.executescript(Path(__file__).with_name("esquema.sql").read_text())
    conexao.executemany(
        "INSERT INTO ativo VALUES (?, ?)", [(1, "D'Ávila"), (2, "Servidor")]
    )
    conexao.execute("INSERT INTO vulnerabilidade VALUES (?, ?, ?)", (1, "DEMO-1", 5))
    conexao.execute("INSERT INTO ativo_vulnerabilidade VALUES (?, ?)", (1, 1))
    try:
        yield conexao
    finally:
        conexao.close()


def test_busca_parametrizada_preserva_nome_legitimo(banco):
    registro = banco.execute(
        "SELECT nome FROM ativo WHERE nome = ?", ("D'Ávila",)
    ).fetchone()
    assert registro == ("D'Ávila",)
    assert banco.execute("SELECT count(*) FROM ativo").fetchone() == (2,)


def test_integridade_referencial(banco):
    with pytest.raises(sqlite3.IntegrityError):
        banco.execute("INSERT INTO ativo_vulnerabilidade VALUES (?, ?)", (99, 1))


def test_join_reduz_consultas_sem_mudar_os_resultados(banco):
    consultas = []
    banco.set_trace_callback(consultas.append)
    ativos = banco.execute("SELECT id, nome FROM ativo ORDER BY id").fetchall()
    por_ativo = [
        (
            nome,
            banco.execute(
                "SELECT vulnerabilidade_id FROM ativo_vulnerabilidade WHERE ativo_id = ?",
                (identificador,),
            ).fetchall(),
        )
        for identificador, nome in ativos
    ]
    assert len(consultas) == 3
    consultas.clear()
    em_lote = banco.execute(
        "SELECT ativo.nome, vinculo.vulnerabilidade_id FROM ativo "
        "LEFT JOIN ativo_vulnerabilidade AS vinculo ON vinculo.ativo_id = ativo.id "
        "ORDER BY ativo.id, vinculo.vulnerabilidade_id"
    ).fetchall()
    assert len(consultas) == 1
    assert por_ativo == [
        (nome, [(item,)] if item is not None else []) for nome, item in em_lote
    ]
