"""Referência de revisão Alembic para o esquema inicial do laboratório."""
from pathlib import Path

from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    esquema = Path(__file__).with_name("esquema.sql").read_text()
    for declaracao in esquema.split(";"):
        if declaracao.strip():
            op.execute(declaracao.strip())


def downgrade():
    op.drop_table("ativo_vulnerabilidade")
    op.drop_table("vulnerabilidade")
    op.drop_table("ativo")
