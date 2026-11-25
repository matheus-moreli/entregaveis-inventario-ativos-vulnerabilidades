# Laboratório independente da aplicação

Na raiz da entrega, execute **python -m pytest laboratorio** para SQLite e autorização. Os testes usam um banco em memória e dados sintéticos.

Para a demonstração complementar, instale as dependências de laboratorio/requirements.txt em um ambiente virtual e execute **python laboratorio/orm_demo.py**. A revisão migracao_0001.py é uma referência para um ambiente Alembic, com esquema.sql ao lado do arquivo. O módulo autenticacao_demo.py permite verificar senhas, chaves aleatórias e JWTs de curta duração em um ambiente isolado. Gere a chave de assinatura fora do código.

A aplicação da UFU continua usando JSON e o Bearer atual. Os exemplos de SQLAlchemy, Alembic, Argon2id e JWT precisam de validação no ambiente com suas dependências.
