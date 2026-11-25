CREATE TABLE ativo (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE vulnerabilidade (
    id INTEGER PRIMARY KEY,
    referencia TEXT NOT NULL UNIQUE,
    cvss REAL NOT NULL CHECK (cvss BETWEEN 0 AND 10)
);

CREATE TABLE ativo_vulnerabilidade (
    ativo_id INTEGER NOT NULL REFERENCES ativo(id),
    vulnerabilidade_id INTEGER NOT NULL REFERENCES vulnerabilidade(id),
    PRIMARY KEY (ativo_id, vulnerabilidade_id)
);
