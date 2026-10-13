"""Exemplo mínimo de herança e polimorfismo usado no Trabalho 2."""


class Ativo:
    """Classe base com os dados que todo ativo possui."""

    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel

    def resumo(self):
        return f"{self.nome} — responsável: {self.responsavel}"


class Servidor(Ativo):
    """Especialização de Ativo que reaproveita o construtor da classe base."""

    def __init__(self, nome, responsavel, sistema_operacional):
        super().__init__(nome, responsavel)
        self.sistema_operacional = sistema_operacional

    def resumo(self):
        return f"{super().resumo()} — servidor {self.sistema_operacional}"


if __name__ == "__main__":
    ativo = Servidor("SRV-WEB-01", "Equipe de TI", "Linux")
    print(ativo.resumo())
