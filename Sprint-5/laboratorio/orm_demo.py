from sqlalchemy import CheckConstraint, Column, ForeignKey, Table, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.orm import relationship, selectinload


class Base(DeclarativeBase):
    pass


vinculos = Table(
    "ativo_vulnerabilidade",
    Base.metadata,
    Column("ativo_id", ForeignKey("ativo.id"), primary_key=True),
    Column("vulnerabilidade_id", ForeignKey("vulnerabilidade.id"), primary_key=True),
)


class Ativo(Base):
    __tablename__ = "ativo"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    vulnerabilidades: Mapped[list["Vulnerabilidade"]] = relationship(secondary=vinculos)


class Vulnerabilidade(Base):
    __tablename__ = "vulnerabilidade"
    __table_args__ = (CheckConstraint("cvss BETWEEN 0 AND 10"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    referencia: Mapped[str] = mapped_column(unique=True)
    cvss: Mapped[float]


if __name__ == "__main__":
    motor = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(motor)
    with Session(motor) as sessao:
        vulnerabilidade = Vulnerabilidade(referencia="DEMO-1", cvss=5)
        sessao.add_all([
            Ativo(nome="Servidor", vulnerabilidades=[vulnerabilidade]),
            Ativo(nome="Notebook", vulnerabilidades=[vulnerabilidade]),
        ])
        sessao.commit()
        consulta = select(Ativo).options(selectinload(Ativo.vulnerabilidades))
        for ativo in sessao.scalars(consulta.order_by(Ativo.id)):
            print(ativo.nome, [item.referencia for item in ativo.vulnerabilidades])
