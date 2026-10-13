"""Exercício autônomo de hierarquia, composição e persistência polimórfica."""

import json
from pathlib import Path


class Vulnerabilidade:
    """Composição: uma ocorrência pertence ao ativo, não é tipo de ativo."""

    def __init__(self, cve, severidade):
        self.cve = cve
        self.severidade = severidade

    def para_dict(self):
        return {"cve": self.cve, "severidade": self.severidade}


class Ativo:
    tipo = "Ativo"

    def __init__(self, identificador, nome, responsavel, vulnerabilidades=None):
        self.id = identificador
        self.nome = nome
        self.responsavel = responsavel
        self.vulnerabilidades = list(vulnerabilidades or [])

    def exibir_detalhes(self):
        return f"{self.tipo} {self.id}: {self.nome} - {self.responsavel}"

    def para_dict(self):
        return {
            "id": self.id, "tipo": self.tipo, "nome": self.nome,
            "responsavel": self.responsavel,
            "vulnerabilidades": [v.para_dict() for v in self.vulnerabilidades],
        }


class Notebook(Ativo):
    tipo = "Notebook"

    def exibir_detalhes(self):
        return super().exibir_detalhes() + " (portátil)"


class Servidor(Ativo):
    tipo = "Servidor"

    def exibir_detalhes(self):
        return super().exibir_detalhes() + " (serviço central)"


class Roteador(Ativo):
    tipo = "Roteador"

    def exibir_detalhes(self):
        return super().exibir_detalhes() + " (rede)"


TIPOS = {classe.tipo: classe for classe in (Notebook, Servidor, Roteador)}


def carregar(caminho):
    """Reconstrói a subclasse e preserva IDs e vínculos com vulnerabilidades."""
    dados = json.loads(Path(caminho).read_text(encoding="utf-8"))
    ativos = []
    for registro in dados:
        classe = TIPOS[registro["tipo"]]
        vulnerabilidades = [Vulnerabilidade(**v) for v in registro["vulnerabilidades"]]
        ativos.append(classe(registro["id"], registro["nome"],
                             registro["responsavel"], vulnerabilidades))
    return ativos


def salvar(ativos, caminho):
    Path(caminho).write_text(
        json.dumps([ativo.para_dict() for ativo in ativos],
                   ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    caminho = Path(__file__).with_name("objetos.json")
    originais = [
        Notebook(1, "NB-LAB-01", "Laboratório",
                 [Vulnerabilidade("CVE-2019-0708", 9.8)]),
        Servidor(2, "SRV-WEB-01", "Infraestrutura",
                 [Vulnerabilidade("CVE-2021-44228", 10.0)]),
        Roteador(3, "RT-FILIAL-01", "Redes"),
    ]
    salvar(originais, caminho)
    recarregados = carregar(caminho)
    assert [type(ativo) for ativo in recarregados] == [type(ativo) for ativo in originais]
    assert [ativo.id for ativo in recarregados] == [1, 2, 3]
    assert recarregados[0].vulnerabilidades[0].cve == "CVE-2019-0708"
    for ativo in recarregados:
        print(ativo.exibir_detalhes(), "| isinstance(Ativo):", isinstance(ativo, Ativo))
    print("JSON recarregado com IDs, subclasses e vínculos preservados.")
