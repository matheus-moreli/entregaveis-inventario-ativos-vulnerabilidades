SELECT a.id, a.nome, v.cve, v.cvss
FROM ativo a
INNER JOIN vulnerabilidade v ON v.ativo_id = a.id;

SELECT a.id, a.nome, v.cve
FROM ativo a
LEFT JOIN vulnerabilidade v ON v.ativo_id = a.id;
