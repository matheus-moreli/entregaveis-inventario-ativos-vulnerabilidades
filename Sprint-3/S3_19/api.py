import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request


CAMINHO_BANCO = Path(__file__).with_name("inventario.db")
CAMINHO_SCHEMA = Path(__file__).with_name("schema.sql")
app = Flask(__name__)


def conexao():
    banco = sqlite3.connect(CAMINHO_BANCO)
    banco.execute("PRAGMA foreign_keys = ON")
    banco.row_factory = sqlite3.Row
    return banco


def iniciar_banco():
    with conexao() as banco:
        banco.executescript(CAMINHO_SCHEMA.read_text(encoding="utf-8"))


@app.after_request
def permitir_frontend(resposta):
    resposta.headers["Access-Control-Allow-Origin"] = "*"
    resposta.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return resposta


@app.get("/ativos")
def listar_ativos():
    with conexao() as banco:
        linhas = banco.execute("SELECT id, nome, tipo, responsavel FROM ativos ORDER BY id").fetchall()
    return jsonify([dict(linha) for linha in linhas])


@app.post("/ativos")
def cadastrar_ativo():
    dados = request.get_json(silent=True) or {}
    nome = str(dados.get("nome", "")).strip()
    tipo = str(dados.get("tipo", "")).strip()
    responsavel = str(dados.get("responsavel", "")).strip()
    if not nome or not tipo:
        return jsonify({"erro": "nome e tipo são obrigatórios"}), 400
    try:
        with conexao() as banco:
            cursor = banco.execute(
                "INSERT INTO ativos (nome, tipo, responsavel) VALUES (?, ?, ?)",
                (nome, tipo, responsavel),
            )
        return jsonify({"id": cursor.lastrowid, "nome": nome, "tipo": tipo}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "nome já cadastrado"}), 409


@app.put("/ativos/<int:identificador>")
def atualizar_ativo(identificador):
    dados = request.get_json(silent=True) or {}
    nome = str(dados.get("nome", "")).strip()
    tipo = str(dados.get("tipo", "")).strip()
    if not nome or not tipo:
        return jsonify({"erro": "nome e tipo são obrigatórios"}), 400
    with conexao() as banco:
        cursor = banco.execute(
            "UPDATE ativos SET nome = ?, tipo = ?, responsavel = ? WHERE id = ?",
            (nome, tipo, str(dados.get("responsavel", "")).strip(), identificador),
        )
    if cursor.rowcount == 0:
        return jsonify({"erro": "ativo não encontrado"}), 404
    return jsonify({"mensagem": "ativo atualizado"})


@app.delete("/ativos/<int:identificador>")
def remover_ativo(identificador):
    with conexao() as banco:
        cursor = banco.execute("DELETE FROM ativos WHERE id = ?", (identificador,))
    if cursor.rowcount == 0:
        return jsonify({"erro": "ativo não encontrado"}), 404
    return "", 204


if __name__ == "__main__":
    iniciar_banco()
    app.run(debug=True)
